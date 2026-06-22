import os
import json
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# Configuration
PORT = 5005
CACHE_FILE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 
    '../memory_bus/coordinator/status/notification_cache.json'
))
MAX_NOTIFICATIONS = 100

class NotificationHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Override to suppress default stdout logging for clean console execution
        pass

    def do_GET(self):
        if self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            status = {
                "status": "online",
                "uptime": time.time(),
                "cache_file": CACHE_FILE,
                "cached_count": self._get_cached_count()
            }
            self.wfile.write(json.dumps(status).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/webhook':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            try:
                payload = json.loads(post_data.decode('utf-8'))
                self._save_notification(payload)
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "message": "Notification cached"}).encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def _get_cached_count(self):
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return len(data)
            except:
                pass
        return 0

    def _save_notification(self, payload):
        os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
        
        # Format the notification object
        notification = {
            "app": payload.get("app", "Unknown"),
            "sender": payload.get("sender", payload.get("title", "Unknown")),
            "message": payload.get("message", payload.get("text", "")),
            "timestamp": payload.get("timestamp", time.strftime("%Y-%m-%dT%H:%M:%S")),
            "received_at": time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        
        notifications = []
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                    notifications = json.load(f)
            except:
                # If JSON is corrupted, reset it
                notifications = []
                
        # Insert at the beginning (newest first)
        notifications.insert(0, notification)
        
        # Keep only the last MAX_NOTIFICATIONS
        notifications = notifications[:MAX_NOTIFICATIONS]
        
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(notifications, f, ensure_ascii=False, indent=2)

def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, NotificationHandler)
    print(f"Notification Bridge listening locally on port {PORT}...")
    print(f"Webhooks can be POSTed to http://localhost:{PORT}/webhook")
    print(f"Notifications will cache to: {CACHE_FILE}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down Notification Bridge...")
        httpd.server_close()

if __name__ == '__main__':
    run()
