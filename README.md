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

<img width="400" height="382" alt="image" src="https://github.com/user-attachments/assets/86b691b2-ab85-408b-96bb-b0b9472ff96a" />


**2. Invalid Email Format**

<img width="400" height="378" alt="image" src="https://github.com/user-attachments/assets/c481b086-fa64-44cc-a186-2a445ee0d736" />


**3. Invalid Age Format**

<img width="400" height="378" alt="image" src="https://github.com/user-attachments/assets/eecc73bf-9094-4417-8c48-410f530d3cdd" />

**4. Invalid Phone Number Length**

![Invalid Phone Number Length](https://github.com/user-attachments/assets/47a82450-66d7-46d3-9127-328a6aafb7f6)

**5. Invalid Phone Number Prefix**

<img width="401" height="381" alt="image" src="https://github.com/user-attachments/assets/ac49dd57-05a3-4a49-81ab-76c85d4c281c" />

**6. Invalid Gender Selection**

<img width="399" height="380" alt="image" src="https://github.com/user-attachments/assets/c8c899d7-6f75-4f91-9316-bb4d1feb95c1" />


**7. Successful Validation**

<img width="399" height="377" alt="image" src="https://github.com/user-attachments/assets/7bc59578-dd38-4b5d-af51-cd9df22c45ae" />


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
└── README.md 
```

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/hndraa/app-FormValidation.git
cd app-FormValidation
```

**2. Install dependencies**

```bash
python -m pip install PyQt5
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
