import urllib.request
import re
from bs4 import BeautifulSoup
import csv
import pickle
import random

topic = "https://en.wikipedia.org/wiki/Momentum"

def links(thepage):
	soup = BeautifulSoup(thepage, features='html.parser')
	try:
		seealsoSection = soup.find('span',{'id':'See_also'})
		# print(seealsoSection)
		seealsolist = seealsoSection.findNext('ul')
		print(seealsolist)
		words = seealsolist.findAll('a')
		# print(words)
		returnwords = []
		for word in words:
			if word['href'].find('wiki/') != -1 and word['href'].find(':') == -1:
				returnwords.append([word.text,'','https://en.wikipedia.org' + word['href']])
	except:
		returnwords = []
	return returnwords


requestingURL = urllib.request.Request(topic, headers={'User-Agent' : "Magic Browser"}) 
page = urllib.request.urlopen(requestingURL).read()

print(links(page))