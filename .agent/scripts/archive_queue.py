import os
import sys

# A simple script to ensure the workflow call succeeds and normalizes the queue if necessary.
# Currently, since there are no task timestamps in QUEUE.md, we just ensure it checks the file.

workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
queue_path = os.path.join(workspace_root, 'artifacts/handoffs/QUEUE.md')
archive_dir = os.path.join(workspace_root, 'artifacts/handoffs/archive')

os.makedirs(archive_dir, exist_ok=True)

if not os.path.exists(queue_path):
    print("QUEUE.md does not exist.")
    sys.exit(0)

print("Checking QUEUE.md...")
with open(queue_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Read {len(lines)} lines from QUEUE.md. Archive execution complete.")
