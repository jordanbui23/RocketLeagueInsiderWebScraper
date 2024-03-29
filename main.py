from bs4 import BeautifulSoup  # If any of these are throwing errors just import the library/package
import requests
import time
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)


# Holds the links for all of the items I want to scrape the prices of
links = [
    "https://rl.insider.gg/en/xbox/octane/white",
    "https://rl.insider.gg/en/xbox/fennec/white",
    "https://rl.insider.gg/en/xbox/interstellar/black",
    "https://rl.insider.gg/en/xbox/zomba/white",
    "https://rl.insider.gg/en/xbox/standard/black"
    ]


def find_price():
    string = "" 
    for item in links:
        html_text = requests.get(item).text                                       # Holds the html prior to being parsed
        soup = BeautifulSoup(html_text, "lxml")                                   # Holds the lxml parsed html
        general = soup.find("tr", id="matrixRow0")                                # The matrix row holds prices for all consoles
        rows = general.find_all("td")                                             # Finds all of the prices in the rows
        price = rows[3].text                                                      # The fourth item in the list is xbox price
        box = soup.find("div", id="sellerOffersContainer")                        # Finds the container holding the name of the item
        name = str(box.h2.text)                                                   # The name is held in here, but needs more formatting
        name = name.replace("[H]", "").replace("[W]", "").replace("Credits", "")  # name is currently formatted like "[H] Titanium White Octane [W] Credits"
        name = name.strip()                                                       # Strip the white space from the name
        string += f"The price for {name} today is {price} credits\n"
    client.messages.create(body=string, from_='+19139149044', to='+19132656747')


if __name__ == "__main__":
    find_price() 
