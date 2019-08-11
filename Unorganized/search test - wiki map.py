import pickle
import pysrt
import re
import wikipediaapi

channels = [	['Physics Girl', 'https://www.youtube.com/user/physicswoman/videos'],
		['Veritasium', 'https://www.youtube.com/user/1veritasium/videos'],
		['Minute Physics', 'https://www.youtube.com/user/minutephysics/videos'],
		['Electroboom', 'https://www.youtube.com/user/msadaghd/videos'],
		['Real Engineering', 'https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg/videos'],
		['Numberphile', 'https://www.youtube.com/user/numberphile/videos'],
		['TedEd', 'https://www.youtube.com/user/TEDEducation/videos'],
		['3Blue1Brown', 'https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw/videos'],
		['Mathologer', 'https://www.youtube.com/channel/UC1_uAIS3r8Vu6JjXWvastJg/videos']	]

searchword = 'Parabola'
hits = 0

wiki_wiki = wikipediaapi.Wikipedia('en')

maintopic = searchword
page_py = wiki_wiki.page(maintopic)

if page_py.exists():
	links = page_py.links
	level1 = []

	for title in sorted(links.keys()):
		if links[title].ns == 0:
			if title not in level1:
				level1.append(title)


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
				for word in level1:
					if re.search(word, sub.text, re.IGNORECASE):
						hits = hits + 1
						print("")
						print(word)
						print(channelName)
						print(videolinknum)
						print(videoname)
						print(videoURL)
						print(sub.text + " : @ " + str(sub.start))
						print(currentsubtype)

				if re.search(word, sub.text, re.IGNORECASE):
					hits = hits + 1
					print("")
					print(searchword)
					print(channelName)
					print(videolinknum)
					print(videoname)
					print(videoURL)
					print(sub.text + " : @ " + str(sub.start))
					print(currentsubtype)


print("")
print("Total Hits")
print(hits)