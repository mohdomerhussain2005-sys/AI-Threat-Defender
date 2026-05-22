import sys
import os

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
    QMessageBox,
    QProgressBar,
    QListWidget
)

from scanner.file_scanner import scan_file


class AntivirusDashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("🛡️ AI Threat Defender")

        self.setGeometry(200, 200, 500, 500)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        # Protection status
        self.status_label = QLabel("✅ Real-Time Protection Active")

        layout.addWidget(self.status_label)

        # Progress label
        self.progress_label = QLabel("Waiting for scan...")

        layout.addWidget(self.progress_label)

        # Progress bar
        self.progress_bar = QProgressBar()

        self.progress_bar.setValue(0)

        layout.addWidget(self.progress_bar)

        # Threat history
        self.threat_history = QListWidget()

        layout.addWidget(self.threat_history)

        # Scan button
        scan_button = QPushButton("Scan Folder")

        scan_button.clicked.connect(self.scan_selected_folder)

        layout.addWidget(scan_button)

        # Exit button
        exit_button = QPushButton("Exit")

        exit_button.clicked.connect(self.close)

        layout.addWidget(exit_button)

        self.setLayout(layout)

    # Scan selected folder
    def scan_selected_folder(self):

        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Select Folder"
        )

        if folder_path:

            dangerous_extensions = [
                ".exe",
                ".bat",
                ".vbs",
                ".ps1",
                ".scr",
                ".cmd"
            ]

            all_files = []

            # Collect all files
            for root, dirs, files in os.walk(folder_path):

                for file in files:

                    all_files.append(
                        os.path.join(root, file)
                    )

            total_files = len(all_files)

            scanned_files = 0

            infected_files = 0

            # Scan files
            for file_path in all_files:

                scanned_files += 1

                filename = os.path.basename(file_path)

                self.progress_label.setText(
                    f"Scanning: {filename}"
                )

                # Progress percentage
                progress = int(
                    (scanned_files / total_files) * 100
                )

                self.progress_bar.setValue(progress)

                QApplication.processEvents()

                # Scan file
                scan_file(file_path)

                _, extension = os.path.splitext(filename)

                if extension.lower() in dangerous_extensions:

                    infected_files += 1

                    self.threat_history.addItem(
                        f"⚠️ Threat: {filename}"
                    )

            # Scan complete message
            QMessageBox.information(
                self,
                "Scan Complete",
                f"""
Scanned Files: {scanned_files}

Threats Detected: {infected_files}
"""
            )

            self.progress_label.setText(
                "✅ Scan Completed"
            )


# Run app
app = QApplication(sys.argv)

window = AntivirusDashboard()

window.show()

sys.exit(app.exec_())