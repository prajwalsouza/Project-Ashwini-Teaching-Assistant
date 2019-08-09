# file = open( "[DownSub.com] .srt", "r")
# lines = file.readlines()
# for linenum in range(0, len(lines)):
# 	print(lines[linenum])

# file.close()

import pysrt
subs = pysrt.open("[DownSub.com] .srt")

for sub in subs:
	print(sub.text)

