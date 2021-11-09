from bs4 import BeautifulSoup
import requests
import time
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
##############################################################

# Holds the links for all of the items I want to keep track of
links = ["https://rl.insider.gg/en/xbox/octane/white",
         "https://rl.insider.gg/en/xbox/fennec/white",
         "https://rl.insider.gg/en/xbox/interstellar/black",
         "https://rl.insider.gg/en/xbox/zomba/white",
         "https://rl.insider.gg/en/xbox/standard/black"
         ]


def find_name_price(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, "lxml")  # Holds the lxml parsed html
    general = soup.find("tr", id="matrixRow0")  # The matrix row holds prices for all consoles
    rows = general.find_all("td")  # Finds all of the prices in the rows
    price = rows[3].text  # The fourth item in the list is xbox price
    box = soup.find("div", id="sellerOffersContainer")  # Finds the container holding the name of the item
    name = str(box.h2.text)  # The name is held in here, but needs more formatting
    # [H] Titanium White Octane [W] Credits
    name = name.replace("[H]", "")
    name = name.replace("[W]", "")
    name = name.replace("Credits", "")
    name = name.strip()  # Strip the white space from the name
    client.messages.create(body=f"The price for {name} today is {price} credits", from_='+19139149044', to='+19132656747')


if __name__ == "__main__":
    while True:
        for item in links:
            find_name_price(item)
        time.sleep(10)  # Time in seconds until it runs the method again
