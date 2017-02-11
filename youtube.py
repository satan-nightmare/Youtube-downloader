#!/usr/bin/python
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
pattern = re.compile(".*yt-uix-tile-link.*")
text=raw_input()
textnew=''
for x in text:
	if x==' ':
		textnew+='+'
	else:
		textnew+=x
#print textnew
url = "https://www.youtube.com/results?search_query=" + textnew
response=urllib2.urlopen(url)
html=response.read()
soup=BeautifulSoup(html,'html.parser')
for vid in soup.find_all("a", class_=pattern):
	print "http://youtube.com"+vid['href']
	break
