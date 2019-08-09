# file = open( "[DownSub.com] .srt", "r")
# lines = file.readlines()
# for linenum in range(0, len(lines)):
# 	print(lines[linenum])

# file.close()
import pickle
import pysrt

channel_name = "Physics Girl"
videonum = 10
filehandler = open("H:\#Everything Else\#Project Ashwini\SRT\\" + channel_name + "\\" + "A-" + channel_name + "-" + str(videonum) + ".p","rb")
check = pickle.load(filehandler)
filehandler.close()


