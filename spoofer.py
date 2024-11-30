import re
import os
import subprocess
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass
from datetime import datetime
from colorama import Fore, Style, init
init()
merah = Fore.LIGHTRED_EX
putih = Fore.LIGHTWHITE_EX
hijau = Fore.LIGHTGREEN_EX
kuning = Fore.LIGHTYELLOW_EX
reset = Style.RESET_ALL
def install_required_modules():
    required_modules = ['termcolor', 'colorama', 'smtplib']
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"{kuning}{module} not found. Installing...{reset}")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
            print(f"{hijau}{module} installed successfully.{reset}")
install_required_modules()
from termcolor import colored
def print_banner():
    banner = f"""
{putih}███╗   ██╗ ██████╗  ██████╗ ██████╗   {putih}A Python Based email {hijau}Spoofer
████╗  ██║██╔═══██╗██╔═══██╗██╔══██╗  {hijau}Version: {putih}v 1.0.0
██╔██╗ ██║██║   ██║██║   ██║██████╔╝  {putih}Author: {hijau}4nuxd [Noob]
██║╚██╗██║██║   ██║██║   ██║██╔══██╗  {hijau}Note: {putih}Every Action Has a Consequence
██║ ╚████║╚██████╔╝╚██████╔╝██████╔╝  {putih}GitHub: {hijau}https://github.com/4nuxd/
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═════╝   {hijau}Bored..? : {putih}http://bit.ly/3MTMHyU
___________________________________________________________________________
    {reset}"""
    print(banner)
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)
def is_valid_username(username):
    return bool(username.strip())
def send_spoofed_email(smtp_server, port, login, password, from_address, to_address, subject, message):
    try:
        email = MIMEMultipart()
        email["From"] = from_address
        email["To"] = to_address
        email["Subject"] = subject
        email.attach(MIMEText(message, "plain"))  # Send as plain text
        print(f"{kuning}\nConnecting to the SMTP server...{reset}")
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(login, password)
            server.sendmail(from_address, to_address, email.as_string())
        print(f"{hijau}\nEmail sent successfully from {from_address} to {to_address}{reset}")
        log_email(from_address, to_address, subject, message)
    except smtplib.SMTPAuthenticationError:
        print(f"{merah}Authentication failed. Please check your username and password.{reset}")
    except smtplib.SMTPConnectError:
        print(f"{merah}Unable to connect to the SMTP server. Check the server address and port.{reset}")
    except smtplib.SMTPException as e:
        print(f"{merah}An error occurred while sending the email: {e}{reset}")
def log_email(from_address, to_address, subject, message):
    log_file = os.path.join(os.getcwd(), "email_log.txt")
    with open(log_file, "a") as file:
        log_entry = (
            f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"From: {from_address}\n"
            f"To: {to_address}\n"
            f"Subject: {subject}\n"
            f"Message:\n{message}\n{'-'*50}\n"
        )
        file.write(log_entry)
    print(f"{hijau}\nEmail details logged successfully in {log_file}.{reset}")
if __name__ == "__main__":
    print_banner()
    print(f"{kuning}=== SMTP Server Configuration ==={reset}")
    smtp_server = input("SMTP Server (e.g., smtp.gmail.com): ").strip()
    port = input("SMTP Port (e.g., 587): ").strip()
    while not port.isdigit() or int(port) not in [25, 465, 587]:
        print(f"{merah}Invalid port. Common SMTP ports are 25, 465, or 587.{reset}")
        port = input("SMTP Port (e.g., 587): ").strip()
    port = int(port)
    login = input("Your SMTP Username (can be email or username): ").strip()
    while not (is_valid_email(login) or is_valid_username(login)):
        print(f"{merah}Invalid username. Please enter a valid email or non-empty username.{reset}")
        login = input("Your SMTP Username (can be email or username): ").strip()
    password = getpass("Your SMTP Password: ")
    print(f"{kuning}\n=== Email Details ==={reset}")
    from_address = input("Spoofed 'From' Address (e.g., fake_sender@example.com): ").strip()
    while not is_valid_email(from_address):
        print(f"{merah}Invalid email format. Please enter a valid spoofed address.{reset}")
        from_address = input("Spoofed 'From' Address (e.g., fake_sender@example.com): ").strip()
    to_address = input("Recipient Email Address: ").strip()
    while not is_valid_email(to_address):
        print(f"{merah}Invalid email format. Please enter a valid recipient address.{reset}")
        to_address = input("Recipient Email Address: ").strip()
    subject = input("Email Subject: ").strip()
    message = input("Email Message (plain text): ").strip()
    send_spoofed_email(smtp_server, port, login, password, from_address, to_address, subject, message)
