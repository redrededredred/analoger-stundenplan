import requests
from auth import auth

AUTH = auth()


class VirtStundenplan:
    def __init__(self):
        self.login_url = "https://virtueller-stundenplan.org/index.php" # POST here

    def login(self, data):
        response = requests.post(self.login_url, data, allow_redirects=True)
        return response.text


if __name__ == "__main__":
    Vs = VirtStundenplan()
    print(Vs.login(AUTH))
else:
    print("Do not use me like that!")