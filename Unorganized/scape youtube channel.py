import time
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import pickle

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
prefs = {"download.default_directory" : "H:\#Everything Else\#Project Ashwini"}
options.add_experimental_option("prefs", prefs)

channelOfInterest = "https://www.youtube.com/user/physicswoman/videos"
channelName = 'Physics Girl'


dirName = "H:\#Everything Else\#Project Ashwini\Channels"

try:
	os.mkdir(dirName)
	print("Directory " , dirName ,  "Created")
except:   
	print("Directory " , dirName ,  " already exists")

dirName = "H:\#Everything Else\#Project Ashwini\Channels\\" + channelName

try:
	os.mkdir(dirName)
	print("Directory " , dirName ,  "Created")
except:   
	print("Directory " , dirName ,  " already exists")

driver = webdriver.Chrome(options=options)
driver.get(channelOfInterest)

videoATagsLen = 0

scrollnumber = 1

while True:
	html = driver.find_element_by_tag_name('html')
	html.send_keys(Keys.END)
	print(str(scrollnumber) + ' scrolls attempted.')
	scrollnumber = scrollnumber + 1
	time.sleep(0.1)
	
	html = driver.page_source
	soup = BeautifulSoup(html.encode('utf-8'), features='html.parser')
	videoATags = soup.findAll("a", {"id": "video-title"})
	if len(videoATags) == videoATagsLen:
		break
	videoATagsLen = len(videoATags)

print("Collected " + str(videoATagsLen) + " links.")

channelVideoLinks = []

for videoATag in videoATags:
	channelVideoLinks.append([videoATag.text, "https://www.youtube.com" + videoATag['href']])

channelData = [channelName, channelOfInterest, channelVideoLinks]

# print(channelData)

filehandler = open("H:\#Everything Else\#Project Ashwini\Channels\\" + channelName + "\\" + channelName + "-Data.p","wb")
pickle.dump(channelData, filehandler)
filehandler.close()


driver.close()
# file = open("Fruits.obj",'rb')
# object_file = pickle.load(file)
# file.close()