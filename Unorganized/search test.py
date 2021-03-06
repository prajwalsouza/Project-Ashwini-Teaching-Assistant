import pickle
import pysrt
import re

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
		['Computerphile', 'https://www.youtube.com/user/Computerphile/videos']	]

searchword = 'projectile'
hits = 0

numberofvideoswithHits = 0
urlIdentifier = ""

for channel in channels:
	channelName = channel[0]
	print("Searching in " + channelName)
	filehandler = open("H:\#Everything Else\#Project Ashwini\Channels\\" + channelName + "\\" + channelName + "-Data.p","rb")
	channelData = pickle.load(filehandler)
	filehandler.close()

	videolinks = channelData[2]


	for videolinknum in range(len(videolinks)):
		videoname = videolinks[videolinknum][0]
		videoURL = videolinks[videolinknum][1]



		subtypes = ['A-', 'C-', 'P-']
		available = False
		for k in range(len(subtypes)):
			try:
				mainfile = pysrt.open("H:\#Everything Else\#Project Ashwini\SRT\\" + channelName + "\\" + subtypes[k] + channelName + "-" + str(videolinknum) + ".srt")
				available = True
				currentsubtype = subtypes[k]
				break
			except:
				None
		if available:
			for sub in mainfile:
				if re.search(searchword, sub.text, re.IGNORECASE):
					hits = hits + 1
					if videoURL != urlIdentifier:
						numberofvideoswithHits = numberofvideoswithHits + 1
						urlIdentifier = videoURL
					print("")
					print(channelName)
					print(videolinknum)
					print(videoname)
					print(videoURL)
					print(sub.text + " : @ " + str(sub.start))
					print(currentsubtype)

print("")
print("Search word : " + searchword)
print(str(hits) + " total hits in " + str(numberofvideoswithHits) + " videos.")