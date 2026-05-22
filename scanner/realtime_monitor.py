from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time

from scanner.file_scanner import scan_file

# Folder to monitor
MONITOR_FOLDER = "monitor_folder"


class ThreatHandler(FileSystemEventHandler):

    def on_created(self, event):

        if not event.is_directory:

            print(f"\n📁 New file detected:")
            print(event.src_path)

            scan_file(event.src_path)


# Setup observer
event_handler = ThreatHandler()

observer = Observer()

observer.schedule(event_handler, MONITOR_FOLDER, recursive=True)

observer.start()

print(f"👀 Monitoring folder: {MONITOR_FOLDER}")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:

    observer.stop()

observer.join()