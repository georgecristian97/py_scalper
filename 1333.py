import urllib.parse
from pygame import mixer
import urllib.request
import time
url001= "https://1337x.to/search/mandalorian+s02e09+2160p/1/"
""" url002= "https://rarbgp2p.org/torrents.php?search=mandalorian+s02e05+2160p"
url003= "https://rarbgp2p.org/torrents.php?search=mandalorian+s02e05+2160p" """
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
values = {
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
       #'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       #'Accept-Encoding': 'none',
       #'Accept-Language': 'en-US,en;q=0.8',
       #'Connection': 'keep-alive'
       }
headers = {'User-Agent': user_agent}


data = urllib.parse.urlencode(values)
data = data.encode('ascii')

while True:
    req001 = urllib.request.Request(url001, data, headers)
    """ req002 = urllib.request.Request(url002, data, headers) """

    print('mandalorian s02e05 2160p')
    with urllib.request.urlopen(req001) as response:
        the_page001 = response.read()
    """ with urllib.request.urlopen(req002) as response:
        the_page002 = response.read()  
    print(the_page002) """
    if b'No results were returned.' in the_page001 :
        print('not found')
        
    else:
        print('found at ',url001)
        break
        
    time.sleep(66*6)
     
mixer.init()      
mixer.music.load('iphone.mp3')
mixer.music.play(-1) 
input('Press enter to stop')