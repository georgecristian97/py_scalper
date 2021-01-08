import urllib.request
import re 
html_content = urllib.request.urlopen('https://1337x.to/search/mandalorian+s02e05+2160p/1/').read()
x = str(html_content)
print(x)

if b'No results were returned. Please refine your search.' in html_content: 
   print ('nol')
   
else:
   print ('I did not find anything')