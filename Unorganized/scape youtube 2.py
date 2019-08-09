import time
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
prefs = {"download.default_directory" : "H:\#Everything Else\#Project Ashwini"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://downsub.com/?url=https://www.youtube.com/watch?v=CSu0cV3fqi8")

html = driver.page_source
soup = BeautifulSoup(html.encode('utf-8'))
maindiv = soup.findAll("div", {"id": "show"})[0]
basicdiv = maindiv.findAll("b")

for div in basicdiv:
	my_text = div.nextSibling
	if(my_text.find("English - CC (English)") != -1):
		print("Found English CC")
		alink = div.find('a')
		driver.find_elements_by_xpath("//a[@href='" + alink['href'] + "']")[0].click()

import time
time.sleep(5)
window_before = driver.window_handles[1]
driver.switch_to_window(window_before)
driver.close()

file = open( "[DownSub.com] .srt", "r")
lines = file.readlines()
for linenum in range(0, len(lines)):
	print(lines[linenum])

file.close()
# python_button = driver.find_elements_by_xpath("//a[@id='Start']")[0]
# python_button.click()