import re
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')
maintopic = 'Mathematical Induction'
page_py = wiki_wiki.page(maintopic)

if page_py.exists():
	links = page_py.links
	print(links)
	level1 = []

	for title in sorted(links.keys()):
		if links[title].ns == 0:
			if title not in level1:
				level1.append(title)
				print(links[title].id)
	print(len(level1))

print(level1)

