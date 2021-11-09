# RocketLeagueInsiderWebScraper
A Rocket League trading website web scraper that texts the user an update on the prices of specified items during specified intervals.

#### Packages/Libraries needed
1. BeautifulSoup
1. lxml
1. Requests

#### APIs used
Twilio SMS

#### How to use Twilio SMS 
1. Create a trial account on Twilio. It should give the user 15 dollars worth of trial credits
1. Once a trial account is created, purchase a twilio phone number.
1. Input the purchased number into "from_='**Purchased Number**'" and the verified user number into "to='**User Number**'".
1. If the user does not have a Twilio verified phone number then the program will not be able to send the user a text alert.
