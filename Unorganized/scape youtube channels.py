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
driver = webdriver.Chrome(options=options)

#Loop1
channels = [	['Physics Girl', 'https://www.youtube.com/user/physicswoman/videos'],
		['Veritasium', 'https://www.youtube.com/user/1veritasium/videos'],
		['Minute Physics', 'https://www.youtube.com/user/minutephysics/videos'],
		['Electroboom', 'https://www.youtube.com/user/msadaghd/videos'],
		['Real Engineering', 'https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg/videos'],
		['Numberphile', 'https://www.youtube.com/user/numberphile/videos'],
		['TedEd', 'https://www.youtube.com/user/TEDEducation/videos'],
		['3Blue1Brown', 'https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw/videos'],
		['Mathologer', 'https://www.youtube.com/channel/UC1_uAIS3r8Vu6JjXWvastJg/videos'],
		['MindYourDecisions', 'https://www.youtube.com/user/MindYourDecisions/videos'],
		['Half as Interesting', 'https://www.youtube.com/channel/UCuCkxoKLYO_EQ2GeFtbM_bw/videos']	]

def check(channelnm):
	exist = False
	try:
		filehandle = open("H:\#Everything Else\#Project Ashwini\Channels\\" + channelnm + "\\" + channelnm + "-Data.p","rb")
		exist = True
	except:
		None

	return exist



for channel in channels:
	channelOfInterest = channel[1]
	channelName = channel[0]

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

	if check(channelName) == False:
		driver.get(channelOfInterest)

		videoATagsLen = 0
		scrollnumber = 1
		while True:
			html = driver.find_element_by_tag_name('html')
			html.send_keys(Keys.END)
			print(str(scrollnumber) + ' scrolls attempted.')
			scrollnumber = scrollnumber + 1
			time.sleep(3)
			html.send_keys(Keys.END)
			print(str(scrollnumber) + ' scrolls attempted.')
			scrollnumber = scrollnumber + 1
			time.sleep(3)
			html.send_keys(Keys.END)
			print(str(scrollnumber) + ' scrolls attempted.')
			scrollnumber = scrollnumber + 1
			time.sleep(3)
			html.send_keys(Keys.END)
			print(str(scrollnumber) + ' scrolls attempted.')
			scrollnumber = scrollnumber + 1
			
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