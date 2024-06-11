from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver

def main():
    inputurl = input("Enter the website here: ")

    driver = get_driver(url=inputurl)

    element = driver.find_element(by="xpath",value='//*[@id="content"]/div/div/div/div[1]/h2')

    return element.text

print(main())