from robobrowser import RoboBrowser
from time import sleep
import random
 
#i=0

#sleep(1)
browser = RoboBrowser(parser='html.parser')
browser.open('http://cyberkeys.us/contact')
#print (random.randint(1,12301983013801932801239))
# Get the signup form
cform = browser.get_form(action='/contact/#wpcf7-f206-p20-o1')
cform['your-name'].value =  str(random.randint(1,12301983013801932801239)-234234)
cform['your-email'].value =  str(random.randint(1,12301983013801932801239))+'@hacker.c'
cform['tel-458'].value =  random.randint(1,12301983013801932801239)-973294729
cform['your-message'].value = str(cform)

#print (cform)
cform.serialize()
browser.submit_form(cform)
#i=i+1
#print ('attack' + str(i))
 
