import bs4
import requests
from bs4 import BeautifulSoup
from auth import auth

AUTH = auth()


class VirtStundenplan:
    def __init__(self):
        self.login_url = "https://www.virtueller-stundenplan.org/page2/index.php" # POST here

    def login(self, data):
        # Login with auth data and process response as html via bs4
        response = requests.post(self.login_url, data, allow_redirects=True)
        return response.url

if __name__ == "__main__":
    Vs = VirtStundenplan()
    print(Vs.login(AUTH))
else:
    print("Do not use me like that!")