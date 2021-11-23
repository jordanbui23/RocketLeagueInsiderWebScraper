# RocketLeagueInsiderWebScraper
A Rocket League trading website web scraper that texts the user an update on the prices of specified items during specified intervals. This is meant for rocket league traders that have a working knowledge of Python.

## Things to node
When uploading to AWS Lambda when it says cannot find lambda_function make sure you are zipping the contents of the folder and not the folder itself.

#### Packages/Libraries needed
1. BeautifulSoup
1. lxml
1. Requests

#### APIs used
- Twilio SMS

#### How to use Twilio SMS 
1. Create a trial account on Twilio. It should give the user 15 dollars worth of trial credits
1. Once a trial account is created, purchase a twilio phone number.
1. Input the purchased number into "from_='**Purchased Number**'" and the verified user number into "to='**User Number**'".
1. If the user does not have a Twilio verified phone number then the program will not be able to send the user a text alert.

#### How to run daily using Amazon AWS
1. Create a new AWS account if you don't already have one
2. Rename the main.py file to lambda_function
3. Rename the function inside to ```def lambda_handler(event, context):```
4. Change
```python
if __name__ == "__main__":
    while True:
        find_price() 
        time.sleep(1000)    
```
To this
```python
if __name__ == "__main__":
    lambda_handler(0, 0)
```
5. Zip the contents **Inside** the folder not the folder itself
6. Create a new AWS Lambda Function and name it whatever you would like
7. Upload the zip folder to the function
8. Once the folder is inside the function you will need an event handler to run the program daily
9. Create an EventBridge (CloudWatch Events) event handler
10. Click on create new rule
11. Enter rule name and description
12. Under rule type schedule expression type rate(1 day)
13. Add the EventBridge and then it should run once a day
