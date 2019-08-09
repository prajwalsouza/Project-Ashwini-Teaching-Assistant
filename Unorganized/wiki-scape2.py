import re
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')
maintopic = 'Center of Mass'
page_py = wiki_wiki.page(maintopic)

if page_py.exists():
	links = page_py.links
	level1 = []

	for title in sorted(links.keys()):
		if links[title].ns == 0:
			if title not in level1:
				level1.append(title)
	print(len(level1))
	level2 = []

	level2connection = []

	count = 0
	for level1node in level1:
		count = count + 1
		page_py2 = wiki_wiki.page(level1node)
		if page_py2.exists():
			links = page_py2.links
			for title in sorted(links.keys()):
				if links[title].ns == 0:
					if title not in level2 and title not in level1:
						level2.append(title)
						level2connection.append([title, level1node])
						print(title + " --> " + level1node + " --> " + maintopic)

		print(count, level1node, len(level2))

print(level1)
print(level2)
print(len(level1), len(level2))

