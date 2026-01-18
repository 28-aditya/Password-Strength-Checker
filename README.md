# Password Strength Checker

A user-friendly desktop application that validates password strength based on industry-standard security requirements.

![Password Strength Checker](images/logo.png)

## Features

- ✅ Real-time password validation
- 🔒 Checks against 10,000+ most common passwords
- 👤 Ensures password doesn't contain user's name
- 📊 Clear, detailed feedback on password requirements
- 🎨 Modern dark-themed UI built with CustomTkinter
- 👁️ Show/hide password toggle

## Password Requirements

Your password must meet ALL of the following criteria:

- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one number
- Contains at least one special character (@, !, #, _, etc.)
- Does not contain your first name
- Does not contain your last name
- Is not in the list of 10,000 most common passwords

## Installation & Usage

### Option 1: Run the Executable (Easiest)

1. Download or locate `Password_Validator_Main.exe`
2. Double-click to run
3. No installation or dependencies required!

### Option 2: Run from Source

#### Requirements

- Python 3.7 or higher
- Required packages:
  - customtkinter
  - Pillow (PIL)

#### Setup

1. Install the required packages:
```bash
pip install customtkinter
pip install Pillow
```

2. Run the application:
```bash
python Password_Validator_Main.py
```

## How to Use

1. **Enter Your Information**
   - Type your first name in the "First Name" field
   - Type your last name in the "Last Name" field

2. **Create Your Password**
   - Enter your desired password in the "Password" field
   - Use the "Show password" checkbox to view what you're typing

3. **Check Password Strength**
   - Click the "Check Password Strength" button
   - View the validation results in the instructions area

4. **Refine Your Password**
   - If your password doesn't meet requirements, the app will show you exactly what's missing
   - The password field will be cleared automatically
   - Simply type a new password and check again!

## Project Structure

```
Password_Strength_Checker/
│
├── Password_Validator_Main.py       # Main entry point
├── Password_Validator_tkinter.py    # GUI implementation
├── Password_Validator.py            # Password validation logic
├── 10k_Most_Common.txt             # Common passwords database
├── README.md                        # This file
│
└── images/
    ├── logo.png                     # Application logo
    └── logo.ico                     # Application icon
```

## File Descriptions

- **Password_Validator_Main.py**: Main application launcher
- **Password_Validator_tkinter.py**: Contains the GUI class and interface design
- **Password_Validator.py**: Core password validation logic and security checks
- **10k_Most_Common.txt**: Database of commonly used passwords to avoid

## Screenshots

### Initial Screen
The app starts with clear instructions and input fields for your information.

### Validation Results
After checking your password, you'll see either:
- ✅ **Success message** (green) if your password meets all requirements
- ❌ **Detailed feedback** (red) listing which requirements aren't met

## Security Features

- Checks against 10,000+ commonly used passwords
- Prevents use of personal information in passwords
- Enforces strong password composition rules
- Local validation only - no data sent over the network

## Building from Source

To create your own executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=images/logo.ico --add-data "10k_Most_Common.txt;." --add-data "images;images" Password_Validator_Main.py
```

The executable will be created in the `dist/` folder.

## Tips for Creating Strong Passwords

- Use a mix of uppercase and lowercase letters
- Include numbers and special characters
- Avoid dictionary words and common patterns
- Don't use personal information
- Aim for at least 12-16 characters (though 8 is the minimum)
- Consider using a passphrase (e.g., "Coffee!Loves2Code#2024")

## Troubleshooting

**Issue**: Application won't start
- **Solution**: Make sure all required files are in the same directory (especially `10k_Most_Common.txt` and the `images/` folder)

**Issue**: "File not found" error when running from source
- **Solution**: Ensure you're running the script from the project directory where all files are located

**Issue**: Validation always fails
- **Solution**: Make sure you've entered both first and last names before checking the password

## License

This project is open source and available for educational purposes.

## Author

Created as a password security educational tool.

## Version

Version 1.0.0

---

**Stay secure! 🔐**