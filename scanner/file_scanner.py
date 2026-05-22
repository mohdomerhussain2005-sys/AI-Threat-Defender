import os
import shutil
import hashlib

# Dangerous file extensions
dangerous_extensions = [
    ".exe",
    ".bat",
    ".vbs",
    ".ps1",
    ".scr",
    ".cmd"
]

# Quarantine folder
QUARANTINE_FOLDER = "quarantine"

# Demo malware hashes
known_malware_hashes = [
    "44d88612fea8a8f36de82e1278abb02f"
]


# Calculate SHA256 hash
def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except:
        return None


# Move file to quarantine
def quarantine_file(file_path):

    filename = os.path.basename(file_path)

    destination = os.path.join(QUARANTINE_FOLDER, filename)

    shutil.move(file_path, destination)

    print(f"📦 File moved to quarantine: {filename}")


# Scan file
def scan_file(file_path):

    filename = os.path.basename(file_path)

    _, extension = os.path.splitext(filename)

    threat_score = 0

    # Check dangerous extension
    if extension.lower() in dangerous_extensions:
        threat_score += 70

    # Suspicious filename
    if "hack" in filename.lower():
        threat_score += 20

    # Hash analysis
    file_hash = calculate_hash(file_path)

    if file_hash in known_malware_hashes:
        threat_score += 100
        print("☠️ Known malware hash detected")

    # Final result
    if threat_score >= 70:

        print(f"\n⚠️ Threat Detected: {filename}")

        quarantine_file(file_path)

    else:
        print(f"\n✅ Safe File: {filename}")