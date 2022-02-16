
# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# method to check a link text is available in home page or not
def checkAvailLinkText(url_text):
    try:
        driver.find_element(By.LINK_TEXT,url_text)
        print("An URL is available for given text",url_text)
    except NoSuchElementException:
        print("The given",url_text,"is not found")

# Chrome web browser will be used
driver = webdriver.Chrome()

# assign university URL and open it using driver
univURL="https://www.lewisu.edu/"

driver.get(univURL)

# retrieve the title of the page and check it
title=driver.title
if(title=="Lewis University"):
    print("The University Webiste contains the title as Lewis University")
else:
    print("The University Website does not contains the title as Lewis University")

# method calls to check the link text is available in the home page or not
checkAvailLinkText("About Us")
checkAvailLinkText("Academics")
checkAvailLinkText("Admission & Aid")
checkAvailLinkText("Athletics")
checkAvailLinkText("Student Life")
checkAvailLinkText("Locations")

# navigate the home page to facult or staff directory
input("Enter a key to navigate to the Fac/Staff directory from home page")
url_fac_staff=driver.find_element(By.LINK_TEXT,"Fac/Staff").get_attribute('href')
driver.get(url_fac_staff)
url_fac_staff_directory=driver.find_element(By.LINK_TEXT,"Faculty/Staff Directory").get_attribute('href')
driver.get(url_fac_staff_directory)

# search the text Omari in the university web site and displays the result
input("Enter a key to search Omari and display result")
searchBox = driver.find_element(By.NAME,"last")
searchBox.send_keys("Omari")
searchBox.send_keys(Keys.RETURN)