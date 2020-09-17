import requests
from bs4 import BeautifulSoup
import smtplib
import time

# url for getting desired data
URL = '{amazon_url_here}'

# headers needed for requests pkg, User-Agent
headers = {
  "User-Agent": '{user_agent_here}'
}

# function that checks the price(s)
def check_price():

  # gets ALL the page data
  page = requests.get(URL, headers=headers)

  # use BS to parse the html
  soup = BeautifulSoup(page.content, 'html.parser')

  # use BS soup propertys' methods to find the data you want
  # .get_text() extracts the text from the html element = string
  # .strip() removes precedding and trailing whitespace
  title = soup.find(id="productTitle").get_text().strip()
  price = soup.find(id="priceblock_saleprice").get_text()
  converted_price = float(price[1:])

  print(title)
  print(converted_price)

  if (converted_price < 15.99):
    send_mail()

# using smtplib to be able to send an email to myself
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  # creates the connection to the email
  server.ehlo()
  # secures the connection
  server.starttls()
  server.ehlo()

  server.login('{email_here}', '{password_here}')

  subject = "Price Dropped!!"
  body = "Check the link!! https://www.amazon.com/Arteck-Ultra-Slim-Bluetooth-Compatible-Including/dp/B07PFCRWG9/ref=pd_di_sccai_2/140-7171811-0447525?_encoding=UTF8&pd_rd_i=B07PFCRWG9&pd_rd_r=33a02dd8-855b-4b3f-b2e0-cc8f49da38b7&pd_rd_w=QyenB&pd_rd_wg=Bagbn&pf_rd_p=5415687b-2c9d-46da-88a4-bbcfe8e07f3c&pf_rd_r=Z6HYQW61A44S4ZHCZ7Y3&psc=1&refRID=Z6HYQW61A44S4ZHCZ7Y3"

  # f"string {expression}" a way to embed expressions within strings
  msg = f"Subject: {subject}\n\n{body}"

  # actually sends the email
  server.sendmail(
    '{from_address_here}',
    '{to_address_here}',
    msg
  )
  print("\nEMAIL WAS SENT!")

  # terminates the server
  server.quit()

# using the time module you can set this server to check the price once each day using a while loop and times' sleep() method
while(True):
  check_price()
  time.sleep(86400)