
import sys
import re

from PyQt5 import QtWidgets, uic, QtGui, QtCore


class FormValidationApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Memuat desain dari Qt Designer
        uic.loadUi("form_validation.ui", self)

        # Placeholder dropdown
        self.genderDropdown.clear()
        self.genderDropdown.addItems([
            "Pilih jenis kelamin",
            "Laki-laki",
            "Perempuan",
            "Tidak ingin memberi tahu"
        ])

        self.educationDropdown.clear()
        self.educationDropdown.addItems([
            "Pilih pendidikan",
            "SMA",
            "Diploma",
            "S1",
            "S2",
            "S3"
        ])

        # Format nomor HP: +62 812 3456 7890
        self.phoneInput.setInputMask("+62 000 0000 0000;_")

        # Menghubungkan tombol
        self.saveButton.clicked.connect(self.validate_form)
        self.clearButton.clicked.connect(self.clear_form)

        # Shortcut untuk keluar: Ctrl + Q
        self.shortcut = QtWidgets.QShortcut(
            QtGui.QKeySequence("Ctrl+Q"), self
        )
        self.shortcut.activated.connect(self.close)

        # Label identitas
        self.identityLabel = QtWidgets.QLabel(
            "hndraa Apps", self
        )
        self.identityLabel.setAlignment(QtCore.Qt.AlignRight)
        self.identityLabel.setStyleSheet(
            "color: white; font-size: 10pt;"
        )
        self.identityLabel.setGeometry(200, 320, 190, 20)

        # Animasi gradien
        self.gradient_position = 0.0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_gradient)
        self.timer.start(50)

    def show_warning(self, message):
        QtWidgets.QMessageBox.warning(
            self, "Validasi Gagal", message
        )

    def validate_form(self):
        name = self.nameInput.text().strip()
        email = self.emailInput.text().strip()
        age = self.ageInput.text().strip()
        address = self.addressInput.toPlainText().strip()

        gender = self.genderDropdown.currentIndex()
        education = self.educationDropdown.currentIndex()

        # Validasi nama dan alamat
        if not name:
            self.show_warning("Nama harus diisi.")
            self.nameInput.setFocus()
            return

        if not address:
            self.show_warning("Alamat harus diisi.")
            self.addressInput.setFocus()
            return

        # Validasi email
        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if not email:
            self.show_warning("Email harus diisi.")
            self.emailInput.setFocus()
            return

        if not re.fullmatch(email_pattern, email):
            self.show_warning("Format email tidak valid.")
            self.emailInput.setFocus()
            return

        # Validasi umur
        if not age:
            self.show_warning("Umur harus diisi.")
            self.ageInput.setFocus()
            return

        if not age.isdigit():
            self.show_warning("Umur harus berupa angka bulat.")
            self.ageInput.setFocus()
            return

        if int(age) <= 0 or int(age) > 120:
            self.show_warning("Umur harus antara 1 dan 120 tahun.")
            self.ageInput.setFocus()
            return

        # Validasi nomor HP
        # Hilangkan karakter selain angka, termasuk +62 dan spasi.
        phone_digits = re.sub(
            r"\D", "", self.phoneInput.text()
        )

        if phone_digits.startswith("62"):
            phone_digits = phone_digits[2:]

        if not phone_digits:
            self.show_warning("Nomor HP harus diisi.")
            self.phoneInput.setFocus()
            return

        if len(phone_digits) != 11:
            self.show_warning(
                "Nomor HP harus memiliki 11 digit setelah +62."
            )
            self.phoneInput.setFocus()
            return

        if not phone_digits.startswith("8"):
            self.show_warning(
                "Nomor HP harus diawali angka 8 setelah +62."
            )
            self.phoneInput.setFocus()
            return

        # Validasi dropdown
        if gender == 0:
            self.show_warning("Silakan pilih jenis kelamin.")
            self.genderDropdown.setFocus()
            return

        if education == 0:
            self.show_warning("Silakan pilih pendidikan.")
            self.educationDropdown.setFocus()
            return

        # Data lolos validasi, belum disimpan secara permanen.
        QtWidgets.QMessageBox.information(
            self,
            "Validasi Berhasil",
            "Semua data valid dan siap diproses."
        )

        self.clear_form()

    def clear_form(self):
        self.nameInput.clear()
        self.emailInput.clear()
        self.ageInput.clear()
        self.phoneInput.clear()
        self.addressInput.clear()

        self.genderDropdown.setCurrentIndex(0)
        self.educationDropdown.setCurrentIndex(0)

        self.nameInput.setFocus()

    def update_gradient(self):
        self.gradient_position += 0.01

        if self.gradient_position > 1:
            self.gradient_position = 0.0

        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        rect = self.rect()

        gradient = QtGui.QLinearGradient(
            0, 0, rect.width(), rect.height()
        )

        value = int(100 + 100 * self.gradient_position)

        gradient.setColorAt(
            0.0, QtGui.QColor(255, value, 200)
        )
        gradient.setColorAt(
            1.0, QtGui.QColor(value, 200, 255)
        )

        painter.fillRect(rect, gradient)
        painter.end()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormValidationApp()
    window.show()
    sys.exit(app.exec_())
