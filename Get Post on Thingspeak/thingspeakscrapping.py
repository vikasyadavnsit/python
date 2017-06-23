import random
import re
import urllib
from bs4 import BeautifulSoup

b= random.randint(0,15000);
# here i am posting data to the field1
data=urllib.urlopen("https://api.thingspeak.com/update?api_key=CLRP7LZ00SCB6GKM&field1="+str(b));
print data;


fed=urllib.urlopen("https://api.thingspeak.com/channels/251862/fields/1.json?results=2");
b=repr(fed.read());
b=b[400:470];
print(b);
m = re.search('field1":"(.+?)"}', b)
if m:
 found=m.group(1)
 print found;
