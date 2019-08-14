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

playlists = [ 	['Tom Scott - Things You Might Not Know', 'https://www.youtube.com/playlist?list=PL96C35uN7xGI9HGKHsArwxiOejecVyNem'],
		['Vox - Vox Observatory', 'https://www.youtube.com/playlist?list=PLJ8cMiYb3G5eNMPb_MTRyLDzm_AOIk7UF'],
		['Vox - Climate Lab', 'https://www.youtube.com/playlist?list=PLJ8cMiYb3G5fP5oq01TBp9fgh70vDDSMe'],
		['Vox - Design', 'https://www.youtube.com/playlist?list=PLJ8cMiYb3G5eD0M1Bfm6lvHy5BR6hoY8X'],
		['Vox - False Positive', 'https://www.youtube.com/playlist?list=PLJ8cMiYb3G5fFn2vF2MvF9Cf6RnaoSZQj'],
		['WIRED - Almost Impossible', 'https://www.youtube.com/playlist?list=PLibNZv5Zd0dweG40QXqhvOk-L1XymbfXi'],
		['WIRED - Obsessed', 'https://www.youtube.com/playlist?list=PLibNZv5Zd0dzFVZ0BvcOZUf0J0Ifn1GeI'],
		['WIRED - Future Tech', 'https://www.youtube.com/playlist?list=PLibNZv5Zd0dzhh9XCT8Wnbi72U9nDW30B']	]
		
			
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
prefs = {"download.default_directory" : "H:\#Everything Else\#Project Ashwini"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

def checkifdownloaded(playlist_name, videonum):
	subtypes = ['A-', 'C-', 'P-', 'F-']
	downloaded = False
	for k in range(len(subtypes)):
		try:
			checkfile = pysrt.open("H:\#Everything Else\#Project Ashwini\SRT - playlists\\" + playlist_name + "\\" + subtypes[k] + playlist_name + "-" + str(videonum) + ".srt")
			downloaded = True
			break
		except:
			None
			# print("H:\#Everything Else\#Project Ashwini\SRT - playlists\\" + playlist_name + "\\" + subtypes[k] + playlist_name + "-" + str(videonum) + ".srt")
	return downloaded


for playlist in playlists:
	playlistName = playlist[0]
	filehandler = open("H:\#Everything Else\#Project Ashwini\playlists\\" + playlistName + "\\" + playlistName + "-Data.p","rb")
	playlistData = pickle.load(filehandler)
	filehandler.close()

	print("Scaping " + playlistName)

	videolinks = playlistData[2]

	dirName = "H:\#Everything Else\#Project Ashwini\SRT - playlists"

	try:
		os.mkdir(dirName)
		print("Directory " , dirName ,  "Created")
	except:   
		print("Directory " , dirName ,  " already exists")

	dirName = "H:\#Everything Else\#Project Ashwini\SRT - playlists\\" + playlistName

	try:
		os.mkdir(dirName)
		print("Directory " , dirName ,  "Created")
	except:   
		print("Directory " , dirName ,  " already exists")

	for videolinknum in range(len(videolinks)):
		videoname = videolinks[videolinknum][0]
		videoURL = videolinks[videolinknum][1]

		

		if checkifdownloaded(playlistName, videolinknum) == False:
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
				file.save("H:\#Everything Else\#Project Ashwini\SRT - playlists\\" + playlistName + "\\" + subtype + playlistName + "-" + str(videolinknum) + ".srt", encoding='utf-8')
				submissing = True
				print("Sub missing")

			elif len(basicdiv) <= 1:
				file = pysrt.SubRipFile()
				sub = pysrt.SubRipItem(1, start='00:00:00,000', end='00:00:01,000', text="Sub was not found")
				file.append(sub)
				subtype = "F-"
				file.save("H:\#Everything Else\#Project Ashwini\SRT - playlists\\" + playlistName + "\\" + subtype + playlistName + "-" + str(videolinknum) + ".srt", encoding='utf-8')
				submissing = True
				print("Sub not found, maybe premium content.")


			if submissing == False:
				print("")
				print(str(videolinknum) + " of " + str(len(videolinks)) + ", from " + playlistName)
				print(videoname)
				print(videoURL)
				print(checkifdownloaded(playlistName, videolinknum))
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
						subs.save("H:\#Everything Else\#Project Ashwini\SRT - playlists\\" + playlistName + "\\" + subtype + playlistName + "-" + str(videolinknum) + ".srt", encoding='utf-8')

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