import pickle
import pysrt
import re
import operator 

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
		['Sci Show', 'https://www.youtube.com/user/scishow/videos']	]

searchword = 'mathematical induction'
hits = 0

numberofvideoswithHits = 0
urlIdentifier = ""

searchedData = {}
searchedDataSpecific = {}

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

		currentHits = 0



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
			sublocations = []
			for sub in mainfile:
				if re.search(searchword, sub.text, re.IGNORECASE):
					hits = hits + 1
					currentHits = currentHits + 1
					if videoURL != urlIdentifier:
						numberofvideoswithHits = numberofvideoswithHits + 1
						urlIdentifier = videoURL

					sublocations.append(sub)
						
					# print("")
					# print(channelName)
					# print(videolinknum)
					# print(videoname)
					# print(videoURL)
					# print(sub.text + " : @ " + str(sub.start))
					# print(currentsubtype)

			if currentHits != 0:
				searchedData[videoname] = [currentHits, channelName, videoname, videoURL, videolinknum, sublocations, currentsubtype]
				searchedDataSpecific[videoname] = currentHits

	print(str(numberofvideoswithHits) + ' videos with hits so far.') 



# newSdata = sorted(searchedData.iteritems(), key = lambda x : x[0])

newSdata = sorted(searchedDataSpecific.items(), key=operator.itemgetter(1))

print("")
print("Results : \n")

for videokey in newSdata:
	sdata = searchedData[videokey[0]]
	print(sdata[1] + " : " + sdata[2] + ", with " + str(sdata[0]) + " hits and subtype " + sdata[6])
	print(sdata[3])
	locs = sdata[5]
	for loc in locs:
		print(loc.text)
		print("at " + str(loc.start))
		print("")

print("")
print("Search word : " + searchword)
print(str(hits) + " total hits in " + str(numberofvideoswithHits) + " videos.")