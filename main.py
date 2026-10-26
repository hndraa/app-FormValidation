
import sys
import re

from PyQt5 import QtWidgets, uic, QtGui, QtCore


class FormValidationApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the user interface designed with Qt Designer
        uic.loadUi("form_validation.ui", self)

        # Configure gender dropdown options
        self.genderDropdown.clear()
        self.genderDropdown.addItems([
            "Select gender",
            "Male",
            "Female",
            "Prefer not to say"
        ])

        # Configure education dropdown options
        self.educationDropdown.clear()
        self.educationDropdown.addItems([
            "Select education",
            "High School",
            "Diploma",
            "Bachelor's Degree",
            "Master's Degree",
            "Doctoral Degree"
        ])

        # Configure the phone number input mask
        self.phoneInput.setInputMask("+62 000 0000 0000;_")

        # Connect buttons to their respective functions
        self.saveButton.clicked.connect(self.validate_form)
        self.clearButton.clicked.connect(self.clear_form)

        # Configure the Ctrl+Q shortcut to close the application
        self.shortcut = QtWidgets.QShortcut(
            QtGui.QKeySequence("Ctrl+Q"), self
        )
        self.shortcut.activated.connect(self.close)

        # Add the developer identification label
        self.identityLabel = QtWidgets.QLabel(
            "hndraa - Apps", self
        )
        self.identityLabel.setAlignment(QtCore.Qt.AlignRight)
        self.identityLabel.setStyleSheet(
            "color: white; font-size: 10pt;"
        )
        self.identityLabel.setGeometry(200, 320, 190, 20)

        # Initialize the animated gradient background
        self.gradient_position = 0.0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_gradient)
        self.timer.start(50)

    def show_warning(self, message):
        """Display a validation warning message."""
        QtWidgets.QMessageBox.warning(
            self, "Validation Error", message
        )

    def validate_form(self):
        """Validate all form fields before accepting the input."""
        name = self.nameInput.text().strip()
        email = self.emailInput.text().strip()
        age = self.ageInput.text().strip()
        address = self.addressInput.toPlainText().strip()

        gender_index = self.genderDropdown.currentIndex()
        education_index = self.educationDropdown.currentIndex()

        # Validate name
        if not name:
            self.show_warning("Name is required.")
            self.nameInput.setFocus()
            return

        # Validate address
        if not address:
            self.show_warning("Address is required.")
            self.addressInput.setFocus()
            return

        # Validate email
        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        if not email:
            self.show_warning("Email address is required.")
            self.emailInput.setFocus()
            return

        if not re.fullmatch(email_pattern, email):
            self.show_warning("Please enter a valid email address.")
            self.emailInput.setFocus()
            return

        # Validate age
        if not age:
            self.show_warning("Age is required.")
            self.ageInput.setFocus()
            return

        if not age.isdigit():
            self.show_warning("Age must be a whole number.")
            self.ageInput.setFocus()
            return

        if int(age) < 1 or int(age) > 120:
            self.show_warning("Age must be between 1 and 120.")
            self.ageInput.setFocus()
            return

        # Validate phone number
        # Remove non-numeric characters, including the country code.
        phone_digits = re.sub(
            r"\D", "", self.phoneInput.text()
        )

        if phone_digits.startswith("62"):
            phone_digits = phone_digits[2:]

        if not phone_digits:
            self.show_warning("Phone number is required.")
            self.phoneInput.setFocus()
            return

        if len(phone_digits) != 11:
            self.show_warning(
                "Phone number must contain 11 digits after +62."
            )
            self.phoneInput.setFocus()
            return

        if not phone_digits.startswith("8"):
            self.show_warning(
                "Phone number must start with 8 after the +62 prefix."
            )
            self.phoneInput.setFocus()
            return

        # Validate gender selection
        if gender_index == 0:
            self.show_warning("Please select a gender.")
            self.genderDropdown.setFocus()
            return

        # Validate education selection
        if education_index == 0:
            self.show_warning("Please select an education level.")
            self.educationDropdown.setFocus()
            return

        # All validation checks have passed
        QtWidgets.QMessageBox.information(
            self,
            "Validation Successful",
            "All form data is valid and ready to be processed."
        )

        self.clear_form()

    def clear_form(self):
        """Clear all input fields and reset dropdown selections."""
        self.nameInput.clear()
        self.emailInput.clear()
        self.ageInput.clear()
        self.phoneInput.clear()
        self.addressInput.clear()

        self.genderDropdown.setCurrentIndex(0)
        self.educationDropdown.setCurrentIndex(0)

        self.nameInput.setFocus()

    def update_gradient(self):
        """Update the gradient animation position."""
        self.gradient_position += 0.01

        if self.gradient_position > 1:
            self.gradient_position = 0.0

        self.update()

    def paintEvent(self, event):
        """Draw the animated gradient background."""
        painter = QtGui.QPainter(self)
        rect = self.rect()

        gradient = QtGui.QLinearGradient(
            0, 0, rect.width(), rect.height()
        )

        color_value = int(
            100 + 100 * self.gradient_position
        )

        gradient.setColorAt(
            0.0,
            QtGui.QColor(255, color_value, 200)
        )
        gradient.setColorAt(
            1.0,
            QtGui.QColor(color_value, 200, 255)
        )

        painter.fillRect(rect, gradient)
        painter.end()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormValidationApp()
    window.show()
    sys.exit(app.exec_())
