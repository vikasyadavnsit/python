from robobrowser import RoboBrowser

browser = RoboBrowser(parser='html.parser')
browser.open('http://www.battleramp.com/contact.htm')

# Get the signup form
cform = browser.get_form(id='contactForm1')
cform['name'].value = 'vikas yadav'
cform['E-mail'].value = 'xyz@hebhagwan.com'
cform['number'].value = 9968001122
cform['country'].value = 'India'
cform['subject'].value = 'Hello vikas'

cform.serialize()
#browser.submit_form(cform)

print ('Sucess') 
