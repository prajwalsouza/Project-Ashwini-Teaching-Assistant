import pickle
import pysrt
import re

channels = [	['Physics Girl', 'https://www.youtube.com/user/physicswoman/videos'],
		['Veritasium', 'https://www.youtube.com/user/1veritasium/videos'],
		['Minute Physics', 'https://www.youtube.com/user/minutephysics/videos'],
		['Electroboom', 'https://www.youtube.com/user/msadaghd/videos'],
		['Real Engineering', 'https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg/videos'],
		['Numberphile', 'https://www.youtube.com/user/numberphile/videos'],
		['TedEd', 'https://www.youtube.com/user/TEDEducation/videos'],	]

searchword = 'complex number'
hits = 0

for channel in channels:
	channelName = channel[0]
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
					print("")
					print(channelName)
					print(videolinknum)
					print(videoname)
					print(videoURL)
					print(sub.text)
					print(currentsubtype)

print("")
print("Total Hits")
print(hits)