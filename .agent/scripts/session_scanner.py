import os
import sys
import json
import shutil
import sqlite3
import time
from datetime import datetime, timedelta

# Configuration
WORKSPACE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
CACHE_FILE = os.path.join(WORKSPACE_ROOT, '.agent/memory_bus/coordinator/status/notification_cache.json')
CONTEXT_OUTPUT = os.path.join(WORKSPACE_ROOT, '.agent/memory_bus/coordinator/status/session_context.json')
TMP_DIR = os.path.join(WORKSPACE_ROOT, '.tmp')

def log_debug(msg):
    print(f"[Scanner Debug] {msg}")

def ensure_dirs():
    os.makedirs(TMP_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(CONTEXT_OUTPUT), exist_ok=True)

def scan_notification_bridge():
    """Reads notification_cache.json for recently synced phone notifications (Zalo, Viber, SeaTalk)"""
    log_debug("Scanning Local Notification Bridge Cache...")
    if not os.path.exists(CACHE_FILE):
        log_debug(f"Cache file not found at {CACHE_FILE}. Notification Bridge is likely empty.")
        return []
    
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            notifications = json.load(f)
            # Filter notifications from last 24 hours
            recent = []
            now = datetime.now()
            for n in notifications:
                try:
                    received_at = datetime.strptime(n.get("received_at", ""), "%Y-%m-%dT%H:%M:%S")
                    if now - received_at < timedelta(hours=24):
                        recent.append(n)
                except Exception as e:
                    # If date parsing fails, keep it anyway
                    recent.append(n)
            log_debug(f"Found {len(recent)} recent notifications in cache.")
            return recent
    except Exception as e:
        log_debug(f"Error reading notification cache: {e}")
        return []

def scan_viber_local_sqlite():
    """Attempts to scan Viber Desktop SQLite database under AppData"""
    log_debug("Scanning Viber Desktop local SQLite database...")
    appdata = os.environ.get('APPDATA')
    if not appdata:
        log_debug("APPDATA environment variable not found. Skipping Viber PC scan.")
        return []
    
    viber_dir = os.path.join(appdata, 'ViberPC')
    if not os.path.exists(viber_dir):
        log_debug("ViberPC AppData directory not found. Skipping Viber PC scan.")
        return []
    
    # Locate phone folders that contain viber.db
    db_paths = []
    for entry in os.listdir(viber_dir):
        full_path = os.path.join(viber_dir, entry)
        if os.path.isdir(full_path):
            db_file = os.path.join(full_path, 'viber.db')
            if os.path.exists(db_file):
                db_paths.append(db_file)
                
    if not db_paths:
        log_debug("No viber.db found inside ViberPC directories. Skipping.")
        return []
    
    # We will query the most recently modified viber.db
    db_paths.sort(key=os.path.getmtime, reverse=True)
    target_db = db_paths[0]
    log_debug(f"Selected target Viber database: {target_db}")
    
    # Copy to tmp to prevent locking
    tmp_db = os.path.join(TMP_DIR, 'viber_temp.db')
    try:
        shutil.copy2(target_db, tmp_db)
    except Exception as e:
        log_debug(f"Failed to copy viber.db to tmp: {e}")
        return []
        
    messages = []
    conn = None
    try:
        conn = sqlite3.connect(tmp_db)
        cursor = conn.cursor()
        
        # Let's inspect the database structure dynamically to make it extremely crash-resistant
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        log_debug(f"Found tables in viber.db: {tables}")
        
        if 'Events' in tables and 'Contact' in tables:
            # Traditional Viber schema
            # Events contains messages. TimeStamp is Unix epoch (sometimes ms or s). Direction 1 is incoming.
            # Let's query incoming messages from last 24 hours
            limit_epoch = int((datetime.now() - timedelta(hours=24)).timestamp())
            
            # Viber sometimes stores timestamps in milliseconds
            cursor.execute("""
                SELECT Contact.Name, Events.Body, Events.TimeStamp 
                FROM Events 
                JOIN Contact ON Events.ContactID = Contact.ContactID 
                WHERE Events.Direction = 1 AND Events.Body IS NOT NULL 
                ORDER BY Events.TimeStamp DESC LIMIT 10
            """)
            rows = cursor.fetchall()
            for r in rows:
                sender, body, ts = r
                # Handle millisecond vs second timestamp
                if ts > 1000000000000:
                    ts = ts / 1000
                messages.append({
                    "app": "ViberPC",
                    "sender": sender,
                    "message": body,
                    "timestamp": datetime.fromtimestamp(ts).strftime("%Y-%m-%dT%H:%M:%S")
                })
        else:
            log_debug("Viber schema unknown or database is encrypted/incompatible.")
    except Exception as e:
        log_debug(f"Error querying Viber database (it may be encrypted): {e}")
    finally:
        if conn:
            conn.close()
        if os.path.exists(tmp_db):
            try:
                os.remove(tmp_db)
            except:
                pass
                
    log_debug(f"Extracted {len(messages)} Viber PC messages.")
    return messages

def scan_google_apis():
    """Placeholder for Google Calendar / Gmail / GDrive integrations.
    Checks for credentials and returns a status warning or fallback values."""
    log_debug("Scanning Google APIs (Calendar, Gmail, GDrive)...")
    google_status = {
        "configured": False,
        "warning": "Google Stack credentials.json not configured in workspace. Showing fallback offline placeholders.",
        "calendar": [],
        "gmail": [],
        "gdrive": []
    }
    
    # We will look for google credentials under .agent/credentials/google_token.json or similar.
    # For now, since credentials are not configured, we provide graceful empty arrays and a warning message.
    # This prevents blocking the workflow while ensuring the UI highlights the configuration warning.
    return google_status

def generate_mock_data():
    """Generates complete, realistic mock data for UI testing and verification"""
    log_debug("Generating mock context data...")
    now = datetime.now()
    
    meetings = [
        {
            "title": "Daily Standup - Team Coby",
            "time": (now + timedelta(hours=2)).strftime("%H:%M") + " - " + (now + timedelta(hours=2, minutes=30)).strftime("%H:%M"),
            "organizer": "Coby Nguyen",
            "link": "https://meet.google.com/abc-defg-hij"
        },
        {
            "title": "B2B Product Strategy Sync",
            "time": "14:00 - 15:00",
            "organizer": "Partnership Team",
            "link": "https://meet.google.com/xyz-uvwx-yza"
        }
    ]
    
    emails = [
        {
            "sender": "Shopee Merchant Services",
            "subject": "Urgent: Update your API webhook endpoint by June 15",
            "received_at": "10:32"
        },
        {
            "sender": "Google Cloud Alert",
            "subject": "[GCP] Budget threshold exceeded for Career-Twin project",
            "received_at": "08:15"
        }
    ]
    
    gdrive = [
        {
            "filename": "OAC_Product_Roadmap_2026.pdf",
            "modified_by": "You",
            "modified_at": "Yesterday"
        },
        {
            "filename": "Weekly_Performance_Metrics.xlsx",
            "modified_by": "AI Analyst",
            "modified_at": "2 hours ago"
        }
    ]
    
    chats = [
        {
            "app": "Zalo",
            "sender": "Anh Minh CEO",
            "message": "Coby ơi, check giúp anh file báo cáo doanh thu tuần trước nhé. Gấp nha!",
            "timestamp": (now - timedelta(minutes=45)).strftime("%Y-%m-%dT%H:%M:%S")
        },
        {
            "app": "ViberPC",
            "sender": "Lan Anh HR",
            "message": "Em đã gửi danh sách ứng viên vòng 2 qua Drive rồi đó.",
            "timestamp": (now - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%S")
        },
        {
            "app": "SeaTalk",
            "sender": "Tech Support Bot",
            "message": "[ALERT] Server backup completed successfully.",
            "timestamp": (now - timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M:%S")
        }
    ]
    
    return {
        "timestamp": now.strftime("%Y-%m-%dT%H:%M:%S"),
        "mode": "MOCK",
        "google": {
            "configured": True,
            "warning": None,
            "calendar": meetings,
            "gmail": emails,
            "gdrive": gdrive
        },
        "chats": chats
    }

def main():
    ensure_dirs()
    
    # Check if mock option is passed
    use_mock = len(sys.argv) > 1 and sys.argv[1] == '--mock'
    
    if use_mock:
        context_data = generate_mock_data()
    else:
        # Run real scans with fallbacks
        notifications = scan_notification_bridge()
        viber_msgs = scan_viber_local_sqlite()
        google_info = scan_google_apis()
        
        # Combine Zalo/Viber notifications with raw Viber local DB
        # To avoid duplicates, we can merge them by message and sender
        combined_chats = []
        seen = set()
        
        # Add Viber PC messages
        for m in viber_msgs:
            key = (m["sender"], m["message"])
            if key not in seen:
                seen.add(key)
                combined_chats.append(m)
                
        # Add notifications (Zalo, SeaTalk, Viber)
        for n in notifications:
            key = (n["sender"], n["message"])
            if key not in seen:
                seen.add(key)
                combined_chats.append({
                    "app": n["app"],
                    "sender": n["sender"],
                    "message": n["message"],
                    "timestamp": n["timestamp"]
                })
                
        # Sort combined chats newest first
        combined_chats.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
        
        context_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "mode": "REAL",
            "google": google_info,
            "chats": combined_chats[:15] # Limit to top 15 messages
        }
        
    # Write aggregated context to session_context.json
    try:
        with open(CONTEXT_OUTPUT, 'w', encoding='utf-8') as f:
            json.dump(context_data, f, ensure_ascii=False, indent=2)
        log_debug(f"Successfully generated context file at: {CONTEXT_OUTPUT}")
    except Exception as e:
        log_debug(f"Error writing context output file: {e}")

if __name__ == '__main__':
    main()
