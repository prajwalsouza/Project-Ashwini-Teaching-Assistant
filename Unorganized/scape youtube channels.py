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
		['Half as Interesting', 'https://www.youtube.com/channel/UCuCkxoKLYO_EQ2GeFtbM_bw/videos'],
		['Welch Labs', 'https://www.youtube.com/user/Taylorns34/videos'],
		['PBS SpaceTime', 'https://www.youtube.com/channel/UC7_gcs09iThXybpVgjHZ_7g/videos'],
		['PBS Infinite Series', 'https://www.youtube.com/channel/UCs4aHmggTfFrpkPcWSaBN9g/videos'],
		['VSauce', 'https://www.youtube.com/user/Vsauce/videos'],
		['Computerphile', 'https://www.youtube.com/user/Computerphile/videos'],
		['Action Lab', 'https://www.youtube.com/channel/UC1VLQPn9cYSqx8plbk9RxxQ/videos'],
		['ASAP Science', 'https://www.youtube.com/user/AsapSCIENCE/videos'],
		['Smarter Everyday', 'https://www.youtube.com/user/destinws2/videos'],
		['Kurzgesagt', 'https://www.youtube.com/user/Kurzgesagt/videos'],
		['Physics Videos by Eugene Khutoryansky', 'https://www.youtube.com/user/EugeneKhutoryansky/videos'],
		['Verge Science', 'https://www.youtube.com/channel/UCtxJFU9DgUhfr2J2bveCHkQ/videos'],
		['Up and Atom', 'https://www.youtube.com/channel/UCSIvk78tK2TiviLQn4fSHaw/videos'],
		['Sixty Symbols', 'https://www.youtube.com/user/sixtysymbols/videos'],
		['Sci Show', 'https://www.youtube.com/user/scishow/videos'],
		['Minute Earth', 'https://www.youtube.com/user/minuteearth/videos'],
		['VSauce2', 'https://www.youtube.com/user/Vsauce2/videos'],
		['VSauce3', 'https://www.youtube.com/user/Vsauce3/videos'],
		['Its Okay To Be Smart', 'https://www.youtube.com/user/itsokaytobesmart/videos'],
		['Looking Glass Universe', 'https://www.youtube.com/user/LookingGlassUniverse/videos'],
		['Mark Rober', 'https://www.youtube.com/user/onemeeeliondollars/videos'],
		['Numberphile2', 'https://www.youtube.com/channel/UCyp1gCHZJU_fGWFf2rtMkCg/videos'],
		['Piled Higher and Deeper', 'https://www.youtube.com/user/phdcomics/videos'],
		['RealLifeLore', 'https://www.youtube.com/channel/UCP5tjEmvPItGyLhmjdwP7Ww/videos'],
		['Seeker', 'https://www.youtube.com/user/DNewsChannel/videos'],
		['Simone Giertz', 'https://www.youtube.com/channel/UC3KEoMzNz8eYnwBC34RaKCQ/videos'],
		['Steve Mould', 'https://www.youtube.com/user/steventhebrave/videos'],
		['The Infographics Show', 'https://www.youtube.com/user/TheInfographicsShow/videos']	]
		

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