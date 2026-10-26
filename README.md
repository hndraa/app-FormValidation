# Form Validation Desktop App

**SOFTWARE | DESKTOP APPLICATION | PYTHON ‧ PYQT5**

A simple desktop application that validates user input through an interactive form. Built with Python and PyQt5, the application provides input validation, dropdown selections, and an animated gradient background.

## 01. Project Overview

### Description
Form Validation is a desktop application developed as part of a Visual Programming practical assignment. It allows users to enter personal information and checks whether the submitted values meet predefined validation rules.

### Objectives
- Practice desktop application development using Python and PyQt5.
- Implement input validation and event-driven programming.
- Design a graphical user interface using Qt Designer.
- Improve user interaction through validation messages and form controls.

### Problems
User input may be incomplete or contain invalid values, such as incorrectly formatted email addresses, non-numeric ages, or improperly formatted phone numbers.

### Solutions
The application validates each field before accepting the form. It displays warning messages when the input does not meet the required rules and provides a clear function to reset the form.

### Key Features
- **Personal Information Form:** Collects name, email, age, phone number, address, gender, and education.
- **Email Validation:** Checks the basic email format.
- **Age Validation:** Accepts whole-number ages within the range of 1–120.
- **Phone Number Validation:** Checks the configured Indonesian phone number format, including the `+62` prefix.
- **Dropdown Selection:** Provides gender and education options.
- **Form Controls:** Supports form validation and clearing all fields.
- **Keyboard Shortcut:** Closes the application using `Ctrl + Q`.
- **Animated Gradient Background:** Adds a simple visual effect to the interface.

## 02. Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and validation |
| PyQt5 | Desktop GUI framework |
| Qt Designer (`.ui`) | User interface design |
| Regular Expressions (`re`) | Email format validation |
| Qt Timer and Painter | Gradient background animation |

## 03. Screenshots / Results

The following screenshots demonstrate the application's interface and validation behavior.

### Initial Interface
<img width="399" height="379" alt="image" src="https://github.com/user-attachments/assets/fbb733b6-8b22-443f-94e5-2abb449c8fca" />

### Validation Scenarios

**1. Empty Form**



**2. Invalid Email Format**

![Invalid Email Validation](https://github.com/user-attachments/assets/f6c54cd9-cb6b-48b5-ad12-72e9e71360e6)

**3. Invalid Age Format**

![Invalid Age Validation](https://github.com/user-attachments/assets/c10da726-c8bc-4bd3-bec9-8c103d66f206)

**4. Invalid Phone Number Length**

![Invalid Phone Number Length](https://github.com/user-attachments/assets/47a82450-66d7-46d3-9127-328a6aafb7f6)

**5. Invalid Phone Number Prefix**

![Invalid Phone Number Prefix](https://github.com/user-attachments/assets/e0c2820e-81d0-481d-9471-ead799f23fc0)

**6. Invalid Gender Selection**

![Invalid Gender Selection](https://github.com/user-attachments/assets/2f559d4a-7021-4fe2-8b72-8d9b8184b476)

**7. Successful Validation**

![image](https://github.com/user-attachments/assets/c3bb31e1-af43-49ef-9e34-9dc8e8be7ae8)

## 04. Installation & Usage

### Prerequisites
- Python 3.12 or later
- pip
- PyQt5

### Project Structure

```text
app-form-validation/
├── main.py
├── form_validation.ui
├── requirements.txt
├── README.md
└── screenshots/
```

The `screenshots/` directory is optional if the screenshots are hosted directly on GitHub, as in the examples above.

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/hndraa/app-form-validation.git
cd app-form-validation
```

**2. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```text
PyQt5
```

**3. Run the application**

```bash
python main.py
```

Ensure that `main.py` and `form_validation.ui` are located in the same directory.

### Usage
1. Launch the application.
2. Enter your personal information in the form.
3. Select your gender and education level.
4. Click **Save** to validate the input.
5. Follow the warning messages if any field is invalid.
6. Click **Clear** to reset the form.
7. Press `Ctrl + Q` to close the application.

### Limitations
- The application performs local input validation only.
- Email validation checks the basic format and does not verify whether the address exists.
- Phone number validation checks the configured format but does not verify the number with a mobile network operator.
- Form data is not permanently stored in a database or file.

---
