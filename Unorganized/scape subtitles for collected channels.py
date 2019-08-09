import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pickle
import pysrt
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys

#Loop1

channels = [['Physics Girl', 'https://www.youtube.com/user/physicswoman/videos'],
		['Veritasium', 'https://www.youtube.com/user/1veritasium/videos'],
		['Minute Physics', 'https://www.youtube.com/user/minutephysics/videos'],
		['Electroboom', 'https://www.youtube.com/user/msadaghd/videos']	]



options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
prefs = {"download.default_directory" : "H:\#Everything Else\#Project Ashwini"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

def checkifdownloaded(channel_name, videonum):
	subtypes = ['A-', 'C-', 'P-']
	downloaded = False
	for k in range(len(subtypes)):
		try:
			filehandler = open("H:\#Everything Else\#Project Ashwini\SRT\\" + channel_name + "\\" + subtypes[k] + channel_name + "-" + str(videonum) + ".p","rb")
			check = pickle.load(filehandler)
			filehandler.close()
			downloaded = True
			break
		except:
			None
	return downloaded




for channel in channels:
	channelName = channel[0]
	filehandler = open("H:\#Everything Else\#Project Ashwini\Channels\\" + channelName + "\\" + channelName + "-Data.p","rb")
	channelData = pickle.load(filehandler)
	filehandler.close()

	print("Scaping " + channelName)

	videolinks = channelData[2]

	dirName = "H:\#Everything Else\#Project Ashwini\SRT"

	try:
		os.mkdir(dirName)
		print("Directory " , dirName ,  "Created")
	except:   
		print("Directory " , dirName ,  " already exists")

	dirName = "H:\#Everything Else\#Project Ashwini\SRT\\" + channelName

	try:
		os.mkdir(dirName)
		print("Directory " , dirName ,  "Created")
	except:   
		print("Directory " , dirName ,  " already exists")

	for videolinknum in range(len(videolinks)):
		videoname = videolinks[videolinknum][0]
		videoURL = videolinks[videolinknum][1]

		print("")
		print(str(videolinknum) + " of " + str(len(videolinks)) + ", from " + channelName)
		print(videoname)
		print(videoURL)
		print(checkifdownloaded(channelName, videolinknum))

		if checkifdownloaded(channelName, videolinknum) == False:
			driver.get("https://downsub.com/?url=" + videoURL)

			html = driver.page_source
			soup = BeautifulSoup(html.encode('utf-8'), features='html.parser')
			maindiv = soup.findAll("div", {"id": "show"})[0]
			basicdiv = maindiv.findAll("b")

			proceed = False
			subtype = ''
			for div in basicdiv:
				my_text = div.nextSibling
				if(my_text.find("CC") != -1):
					print("Found English CC")
					alink = div.find('a')
					driver.find_elements_by_xpath("//a[@href='" + alink['href'] + "']")[0].click()
					proceed = True
					subtype = 'C-'
					break

			
			if proceed == False:
				for div in basicdiv:
					my_text = div.nextSibling
					if(my_text.find("English") != -1):
						print("Found English Plain")
						alink = div.find('a')
						driver.find_elements_by_xpath("//a[@href='" + alink['href'] + "']")[0].click()
						subtype = 'P-'
						proceed = True
						break

			if proceed == False:		
				for div in basicdiv:
					my_text = div.nextSibling
					if(my_text.find("English (auto-generated)") != -1):
						print("Found English Auto")
						alink = div.find('a')
						driver.find_elements_by_xpath("//a[@href='" + alink['href'] + "']")[0].click()
						subtype = 'A-'
						proceed = True
						break
						
			if proceed:	
				time.sleep(5)
				
				subs = pysrt.open("[DownSub.com] .srt")
				subtitles = []
				for sub in subs:
					subtitles.append(sub)

				time.sleep(3)

				if os.path.exists("[DownSub.com] .srt"):
					os.remove("[DownSub.com] .srt")
				else:
					print("The file does not exist")

				filehandler = open("H:\#Everything Else\#Project Ashwini\SRT\\" + channelName + "\\" + subtype + channelName + "-" + str(videolinknum) + ".p","wb")
				pickle.dump(subtitles, filehandler)
				filehandler.close()
		else:
			print("Already Downloaded.")



driver.close()

# window_before = driver.window_handles[1]
# driver.switch_to_window(window_before)
# driver.close()

# driver.switch_to_window(driver.window_handles[0])