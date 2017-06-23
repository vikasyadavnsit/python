import urllib
from bs4 import BeautifulSoup

data=urllib.urlopen("https://www.timeanddate.com/worldclock/india/new-delhi");

soup=BeautifulSoup(data,"html.parser");

time=soup.find(id="ct");
date =soup.find(id="ctdat");


print time.string , " " , date.string;
