# Email Spoofer - Python Based SMTP Mailer 📧💻

## Overview 🌐
This is a Python-based SMTP mailer tool designed for educational purposes. It allows you to send spoofed emails through an SMTP server by providing the necessary SMTP configuration (server, port, login, password) and email details (from address, to address, subject, message). The script supports both plain text and HTML email content. 

### Version: 1.0.1
### Author: Noob Pirate aka Blionrie 🏴‍☠️

## Features ✨
- Send spoofed emails using any SMTP server (e.g., Gmail, Yahoo, etc.)
- Option to include HTML content in the email 📝
- Logs all sent emails to a file for record-keeping 📂
- Handles common SMTP errors (authentication, connection issues, etc.) ⚠️
- Simple CLI interface with color-coded outputs for success and error messages 🎨

## Requirements 🛠️
- Python 3.x
- `termcolor` and `colorama` for colored terminal output 🎨
- `smtplib` for sending emails (usually comes with Python by default)

### Required Python Modules 📦
- `termcolor`
- `colorama`
- `smtplib` (usually included in Python)

## Installation 🚀

### Install Required Modules
Before using the tool, make sure the necessary Python modules are installed. You can install them using the following commands:

```bash
pip install termcolor colorama
```

The script automatically installs missing modules when executed. 🔧

## Usage 💡

### 1. Clone or Download the Script 📥

Clone this repository or download the script `spoofer.py`.

### 2. Prepare HTML Content (Optional) 🖥️
If you wish to send an HTML email, create an HTML file called `msg.html` in the same directory as the script. The script will automatically read this file when prompted to send HTML content. Example:

```html
<!-- msg.html -->
<html>
  <body>
    <h1>This is a spoofed email!</h1>
    <p>This is the HTML content of the email.</p>
  </body>
</html>
```

### 3. Run the Script 🏃

Execute the script from the terminal or command prompt:

```bash
python spoofer.py
```

The script will prompt you for the following inputs:
- **SMTP Server**: The SMTP server address (e.g., smtp.gmail.com).
- **SMTP Port**: The SMTP port number (commonly 25, 465, or 587).
- **SMTP Username**: Your email or username used to authenticate with the SMTP server.
- **SMTP Password**: Your SMTP password (input will be hidden).
- **From Address**: The email address you want to spoof.
- **To Address**: The recipient email address.
- **Subject**: The subject of the email.
- **Message**: The plain text body of the email.
- **HTML Content**: Choose whether to include HTML content. If you answer `yes`, the script will automatically look for `email_content.html` in the same directory.

### Example:

```bash
SMTP Server (e.g., smtp.gmail.com): smtp.gmail.com
SMTP Port (e.g., 587): 587
Your SMTP Username (can be email or username): example@gmail.com
Your SMTP Password: ********
Spoofed 'From' Address (e.g., fake_sender@example.com): fake_sender@example.com
Recipient Email Address: victim@example.com
Email Subject: Test Email
Email Message (plain text): This is a test email.
Do you want to include HTML content? (yes/no): yes
```

### 4. Email Logging 📓
The script logs all sent emails in a file called `email_log.txt` in the current directory. Each log entry includes the time, sender, recipient, subject, and message content.

## Troubleshooting ⚠️
- **Authentication Failed**: Ensure your SMTP username and password are correct. 🔑
- **Connection Error**: Verify the SMTP server address and port. 🌐
- **HTML File Missing**: If you choose to include HTML content but don't have an `email_content.html` file in the same directory, the script will notify you. 📄

## Disclaimer 🚨
This tool is intended for educational purposes only. Please do not use it for malicious activities or spam. Always ensure you have permission before sending emails on behalf of others. ⚖️

## License 📝
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
