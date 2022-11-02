import getpass
import sys

# Add authentication-code here

# Extremely unsafe and will change later


def auth():
    login = input("Login: ")
    password = input("Secret: ")
    return f"MAIL={login}&SCHUELERCODE={password}"

