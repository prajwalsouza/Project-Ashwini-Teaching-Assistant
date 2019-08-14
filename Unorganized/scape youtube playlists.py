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
playlists = [ 	['Tom Scott - Things You Might Not Know', 'https://www.youtube.com/playlist?list=PL96C35uN7xGI9HGKHsArwxiOejecVyNem'],
		['Vox - Vox Observatory', 'https://www.youtube.com/playlist?list=PLJ8cMiYb3G5eNMPb_MTRyLDzm_AOIk7UF'],
		['Vox - Climate Lab', 'https://www.youtube.com/playlist?list=PLJ8cMiYb3G5fP5oq01TBp9fgh70vDDSMe'],
		['Vox - Design', 'https://www.youtube.com/playlist?list=PLJ8cMiYb3G5eD0M1Bfm6lvHy5BR6hoY8X'],
		['Vox - False Positive', 'https://www.youtube.com/playlist?list=PLJ8cMiYb3G5fFn2vF2MvF9Cf6RnaoSZQj'],
		['WIRED - Almost Impossible', 'https://www.youtube.com/playlist?list=PLibNZv5Zd0dweG40QXqhvOk-L1XymbfXi'],
		['WIRED - Obsessed', 'https://www.youtube.com/playlist?list=PLibNZv5Zd0dzFVZ0BvcOZUf0J0Ifn1GeI'],
		['WIRED - Future Tech', 'https://www.youtube.com/playlist?list=PLibNZv5Zd0dzhh9XCT8Wnbi72U9nDW30B']	]
		

def check(playlistnm):
	exist = False
	try:
		filehandle = open("H:\#Everything Else\#Project Ashwini\playlists\\" + playlistnm + "\\" + playlistnm + "-Data.p","rb")
		exist = True
	except:
		None

	return exist



for playlist in playlists:
	playlistOfInterest = playlist[1]
	playlistName = playlist[0]

	dirName = "H:\#Everything Else\#Project Ashwini\playlists"

	try:
		os.mkdir(dirName)
		print("Directory " , dirName ,  "Created")
	except:   
		print("Directory " , dirName ,  " already exists")

	dirName = "H:\#Everything Else\#Project Ashwini\playlists\\" + playlistName

	try:
		os.mkdir(dirName)
		print("Directory " , dirName ,  "Created")
	except:   
		print("Directory " , dirName ,  " already exists")

	if check(playlistName) == False:
		driver.get(playlistOfInterest)

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
			videoATags = soup.findAll("a", {"class": "yt-simple-endpoint style-scope ytd-playlist-video-renderer"})
			if len(videoATags) == videoATagsLen:
				break
			videoATagsLen = len(videoATags)

		print("Collected " + str(videoATagsLen) + " links.")

		playlistVideoLinks = []

		for videoATag in videoATags:
			nameinfo = videoATag.find("span", {"id": "video-title"})
			playlistVideoLinks.append([nameinfo.text, "https://www.youtube.com" + videoATag['href']])
			# print(nameinfo.text)

		playlistData = [playlistName, playlistOfInterest, playlistVideoLinks]

		# print(playlistData)

		filehandler = open("H:\#Everything Else\#Project Ashwini\playlists\\" + playlistName + "\\" + playlistName + "-Data.p","wb")
		pickle.dump(playlistData, filehandler)
		filehandler.close()

driver.close()
# file = open("Fruits.obj",'rb')
# object_file = pickle.load(file)
# file.close()