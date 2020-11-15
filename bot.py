from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# right now this bot is configured for ps4 1 tb slim
# comment second url out and use the first one for ps5

# driver.get("https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815")
driver.get("https://www.walmart.com/ip/Sony-PlayStation-4-1TB-Slim-Gaming-Console/101507200")

# delay in seconds (bot waits <delay> seconds for the page to load)
delay = 3

time.sleep(delay)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div[1]/section/div[1]/div[3]/button/span/span').click()

time.sleep(delay)
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/button[1]').click()

time.sleep(delay)
driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button').click()

time.sleep(delay)
driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button').click()

time.sleep(delay)

# Type your name (capitalized)
first_name = ""
element = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[1]/div[2]/input')
element.clear()
element.send_keys(first_name)

# Type your street address (just the number and road)
street_address = ""
element = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[2]/div[1]/input')
element.clear()
element.send_keys(street_address)

# Type your last name (capitalized)
last_name = ""
element = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[1]/div[3]/input')
element.clear()
element.send_keys(last_name)

# Type apartment number (leave as "" if no apt number)
apt = ""
element = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[2]/div[2]/input')
element.clear()
element.send_keys(apt)

# Type phone number (ten straight digits)
phone_number = ""
element = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[1]/div[4]/input')
element.clear()
element.send_keys(phone_number)

# Type your city
city = ""
element = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[2]/div[3]/input')
element.clear()
element.send_keys(city)

# Type your email
email_address = ""
element = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[1]/div[5]/div/input')
element.clear()
element.send_keys(email_address)

# Type your state abbreviation (capitalized ie IL or OH)
state = ""
driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[2]/div[4]/div[1]/div/select')
for i in range(1, 61):
  curr_state = '/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[2]/div[4]/div[1]/div/select/option[' + str(i) + ']'
  element = driver.find_element_by_xpath(curr_state)
  if element.get_attribute("value") == state:
    element.click()
    break

# Type your five digit zipcode
zip_code = ""
element = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[1]/div[2]/div[4]/div[2]/div/input')
element.clear()
element.send_keys(zip_code)

driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[1]/div/div[2]/div/label/input').click()

driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[2]/div[2]/button').click()
time.sleep(delay)

# Type your credit card number (no spaces)
credit_card = ""
element = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[1]/div/div[3]/input')
element.clear()
element.send_keys(credit_card)

# Type two digit month of expiry (ie 02 or 11)
month = ""
for i in range(1,14):
  curr_month = '/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[1]/span/div/select/option[' + str(i) + ']'
  element = driver.find_element_by_xpath(curr_month)
  if element.get_attribute("value") == month:
    element.click()
    break

# Type last two digits of year of expiry (2024 -> 24, 2021 -> 21, etc)
year = ""
for i in range(1,13):
  curr_year = '/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[2]/span/div/select/option[' + str(i) + ']'
  element = driver.find_element_by_xpath(curr_year)
  if element.get_attribute("value") == year:
    element.click()
    break

# Type cvv (3 or 4 digits)
cvv = ""
element = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[1]/div/div[4]/div[2]/div/div/div/input")
element.clear()
element.send_keys(cvv)

# time.sleep(delay)

# driver.close()
