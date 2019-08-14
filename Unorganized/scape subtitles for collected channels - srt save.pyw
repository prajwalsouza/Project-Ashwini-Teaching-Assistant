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
		['The Infographics Show', 'https://www.youtube.com/user/TheInfographicsShow/videos'],
		['Deep Look', 'https://www.youtube.com/user/KQEDDeepLook/videos']	]

		
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
prefs = {"download.default_directory" : "H:\#Everything Else\#Project Ashwini"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

def checkifdownloaded(channel_name, videonum):
	subtypes = ['A-', 'C-', 'P-', 'F-']
	downloaded = False
	for k in range(len(subtypes)):
		try:
			checkfile = pysrt.open("H:\#Everything Else\#Project Ashwini\SRT\\" + channel_name + "\\" + subtypes[k] + channel_name + "-" + str(videonum) + ".srt")
			downloaded = True
			break
		except:
			None
			# print("H:\#Everything Else\#Project Ashwini\SRT\\" + channel_name + "\\" + subtypes[k] + channel_name + "-" + str(videonum) + ".srt")
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
		print("Directory " , dirName ,  " created")
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

		

		if checkifdownloaded(channelName, videolinknum) == False:
			while True:
				try:
					driver.get("https://downsub.com/?url=" + videoURL)
					html = driver.page_source
					soup = BeautifulSoup(html.encode('utf-8'), features='html.parser')
					maindiv = soup.findAll("div", {"id": "show"})[0]
					basicdiv = maindiv.findAll("b")
					break
				except:
					# html = driver.find_element_by_tag_name('html')
					time.sleep(1)
					driver.refresh()

			submissing = False
			if html.find("Sorry, there are no subtitle available for this video.") != -1:
				file = pysrt.SubRipFile()
				sub = pysrt.SubRipItem(1, start='00:00:00,000', end='00:00:01,000', text="Sub was not found")
				file.append(sub)
				subtype = "F-"
				file.save("H:\#Everything Else\#Project Ashwini\SRT\\" + channelName + "\\" + subtype + channelName + "-" + str(videolinknum) + ".srt", encoding='utf-8')
				submissing = True
				print("Sub missing")

			elif len(basicdiv) <= 1:
				file = pysrt.SubRipFile()
				sub = pysrt.SubRipItem(1, start='00:00:00,000', end='00:00:01,000', text="Sub was not found")
				file.append(sub)
				subtype = "F-"
				file.save("H:\#Everything Else\#Project Ashwini\SRT\\" + channelName + "\\" + subtype + channelName + "-" + str(videolinknum) + ".srt", encoding='utf-8')
				submissing = True
				print("Sub not found, maybe premium content.")


			if submissing == False:
				print("")
				print(str(videolinknum) + " of " + str(len(videolinks)) + ", from " + channelName)
				print(videoname)
				print(videoURL)
				print(checkifdownloaded(channelName, videolinknum))
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
						if(my_text.find("English") != -1 and my_text.find("English (auto-generated)") == -1):
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
					
					try:
						subs = pysrt.open("[DownSub.com] .srt")
						subs.save("H:\#Everything Else\#Project Ashwini\SRT\\" + channelName + "\\" + subtype + channelName + "-" + str(videolinknum) + ".srt", encoding='utf-8')

						time.sleep(1)

						if os.path.exists("[DownSub.com] .srt"):
							os.remove("[DownSub.com] .srt")
						else:
							print("The file does not exist")
					except:
						print("Download Missed.")
		# else:
		# 	print("Already Downloaded.")



driver.close()

# window_before = driver.window_handles[1]
# driver.switch_to_window(window_before)
# driver.close()

# driver.switch_to_window(driver.window_handles[0])