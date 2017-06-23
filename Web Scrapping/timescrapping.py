import urllib
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormtrse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,"html.parser");
#print(soup.prettify);
#print(soup.a);
#print(soup.find_all('a'));
#print(soup.head)
#print(soup.head.string)
#print(soup.find_all('p'));
#print(soup.find(id="link1").string);
#for link in soup.find_all('a'):
# print(link.get('href'));
#print(soup.get)
#print(soup.find(id="link3").string);

data=urllib.urlopen("https://www.timeanddate.com/worldclock/india/new-delhi");
soup=BeautifulSoup(data,"html.parser");
time=soup.find(id="ct");
date=soup.find(id="ctdat");
#wl = soup.find_all(attrs={"class":"offset-4"})
weather=soup.find(id="wt-tp");
print"time in New Delhi :" ,time.string,"Date :" ,date.string ,"Temperature:",weather.string;



