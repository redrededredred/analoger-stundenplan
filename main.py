from datetime import datetime
import bs4
import requests
from bs4 import BeautifulSoup
from auth import auth

AUTH = auth()


class VirtStundenplan:
    def __init__(self, auth_data, for_date="01.01.1970"):
        self.auth_data = auth_data
        self.login_url = "https://www.virtueller-stundenplan.org/index.php" # POST here
        schoolday = datetime.now().strftime("%d.%m.%Y") # Current date or the url
        if for_date == "01.01.1970":
            self.data_url = "https://www.virtueller-stundenplan.org/page2/index.php?KlaBuDatum=" + schoolday # GET data here
        else:
            self.data_url = "https://www.virtueller-stundenplan.org/page2/index.php?KlaBuDatum=" + for_date # GET data here
        

    def scrape(self):
        # Login with auth data and return response as html
        with requests.Session() as session:
            # Authenticate the session
            session.post(self.login_url, self.auth_data, allow_redirects=True)
            # Get raw_html
            raw_html = session.get(self.data_url).text
            if "Digitaler Ausweis" in raw_html:
                return raw_html
            else:
                return False

    def get(self):
        raw_html = self.scrape()
        # Check if login succeeded
        if raw_html:
            # Use bs4 to work with the html and extract important data
            soup = bs4.BeautifulSoup(raw_html, "html.parser")
            data = []
            for item in soup.find(class_="tab-content"):
                data.append(item.text)
            # clean up date and store in an dictionary

            teachers = data[1].strip()
            subjects = data[4].strip()
            rooms = data[7].strip()
            tests = data[10].strip()
            
            clean_data = {
                "date": teachers[4:6] + " " + teachers[6:11], # Date is identical in each data-array from above
                "teachers":teachers, 
                "subjects":subjects,
                "rooms":rooms,
                "tests":tests, # Requires special check lenght is dynamic
            }
            
            

            return clean_data
        # TODO: Move this check to scrape function
        else:
            return "Login unsuccessful!"


if __name__ == "__main__":
    Vs = VirtStundenplan(AUTH, for_date="12.11.2022")
    print(Vs.get())
else:
    print("Do not use me like that!")