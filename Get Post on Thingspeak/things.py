import urllib
import re
from bs4 import BeautifulSoup

#data=urllib.urlopen("https://api.thingspeak.com/update?api_key=EDLC8KHZZ4EV4KKZ&field1="+str(900));
#print data;


datafromwebsite=urllib.urlopen("https://api.thingspeak.com/channels/289288/feeds.json?results=2");
select=repr(datafromwebsite.read());
select=select[300:];

pick=re.search('field1":"(.+?)",',select);
if pick:
 print pick.group(1);

