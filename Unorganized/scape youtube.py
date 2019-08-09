import time
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
# import requests 

# r = requests.get() 
# print(r.content) 

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("download.default_directory='H:\#Everything Else\#Project Ashwini'")



# profile.AddUserProfilePreferences("browser.download.folderList", 2)
# profile.AddUserProfilePreferences("browser.download.manager.showWhenStarting", False)
# profile.AddUserProfilePreferences("browser.download.dir", 'H:\#Everything Else\#Project Ashwini')
prefs = {
"download.default_directory" : "H:\#Everything Else\#Project Ashwini"
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://downsub.com/?url=https://www.youtube.com/watch?v=CSu0cV3fqi8")

html = driver.page_source
# print(html)
soup = BeautifulSoup(html.encode('utf-8'))
maindiv = soup.findAll("div", {"id": "show"})[0]
basicdiv = maindiv.findAll("b")

for div in basicdiv:
	my_text = div.nextSibling
	# print(div.find('a'))
	if(my_text.find("English - CC (English)") != -1):
		# prefs = {"download.default_directory" : "H:\#Everything Else\#Project Ashwini"}
		# options.add_experimental_option("prefs", prefs)
		alink = div.find('a')
		# print(alink)
		driver.find_elements_by_xpath("//a[@href='" + alink['href'] + "']")[0].click()

# options.add_argument("download.default_directory=C:/Downloads")
# profile = webdriver.Profile()


# options.set_preference('browser.download.folderList', 2) # custom location
# options.set_preference('browser.download.manager.showWhenStarting', False)
# options.set_preference('browser.download.dir', '/tmp')

# python_button = driver.find_elements_by_xpath("//a[@id='Start']")[0]
# python_button.click()