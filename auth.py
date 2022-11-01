import getpass
import sys

# Add authentication-code here

# Extremely unsafe and will change later


def auth():
    login = input("Login: ")
    password = input("Secret: ")
    return {"MAIL": login, "SCHUELERCODE": password}