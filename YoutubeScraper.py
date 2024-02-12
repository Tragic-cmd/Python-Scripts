# This script can be used on a youtube profile to scroll all the way down a page and record video data

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

import time

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.youtube.com/@SomeOrdinaryGamers/videos')

# driver.find_element_by_tag_name('body').send_keys(Keys.END)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

for _ in range(3):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(3)

html = driver.page_source

soup = BeautifulSoup(html,'html.parser')

Videos = soup.find_all('div',("id", "dismissible"))

len(Videos)

driver.get('')

for _ in range(5):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(3)













