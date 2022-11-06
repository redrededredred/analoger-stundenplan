import getpass
import sys

# Add authentication-code here

# Extremely unsafe and will change later


def auth():
    login = input("Login: ")
    password = getpass.getpass()
    return {"MAIL": login, "SCHUELERCODE": password, "formAction": "login", "formName": "stacks_in_368_page1"}

