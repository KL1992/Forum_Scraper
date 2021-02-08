import urllib
import urllib.request
import re, datetime
import _string
import uuid
import mysql.connector
from mysql.connector import Error
from urllib.request import Request
from bs4 import BeautifulSoup
from urllib.error import HTTPError


#aaa
#this for loop iterates over each forum page, the indicies from the loop feed into theurl string
for pagenum in range(584,585):
  
  #each url will need tailoring since each forum formats their pages differently
  theurl = "https://www.7thgenhonda.com/forum/printthread.php?t=44&pp=10&page=" + str(pagenum)
  #below are the soup calls to open the webpage and spoof any anti-botting hurdles
  theheader = {'User-Agent': 'Mozilla/5.0'}
  req = Request(theurl, headers = theheader)
  thepage = urllib.request.urlopen(req)
  soup = BeautifulSoup(thepage,"html.parser")  

  #this for loop goes through the webpage and parses out each element and finds the picture links
  for img in soup.findAll('img'):
    stringx = str(img.get('data-url'))
    
    if 'photobucket' in stringx:      
        #print(stringx)
        cleanURL = stringx.split('.', maxsplit=1)
        #print(cleanURL[1])
        genericURL = 'https://www.'
        fullURL = genericURL + cleanURL[1]
        #print("this is the full URL found:" + fullURL)
        executeDownload(fullURL)
    elif stringx.startswith("http"): 
        executeDownload(stringx)    
    #postinfo = str(img.findNext('div', class_='message-userContent lbContainer js-lbContainer')['data-lb-caption-desc'])
    #cleanusername = postinfo.split('·', maxsplit=1) 
    #datePosted = cleanusername[1].split('at',maxsplit=1)  
    #print(str(cleanusername[0]))        
    #print(str(datePosted[0]))
    #if 'flickr' in stringx and 'static' not in stringx:
    
        

    #print(stringx)
    #this if statement filters out all the dead links on the page by comparing url names with valid websites 
    def executeDownload(stringxx):
        postinfo = str(img.findPrevious('div', class_='message-userContent lbContainer js-lbContainer')['data-lb-caption-desc'])
        cleanusername = postinfo.split('·', maxsplit=1) 
        datePosted = cleanusername[1].split('at',maxsplit=1)  
        print(str(cleanusername[0]))        
        print(str(datePosted[0]))
        print(stringxx)

      #postinfo = a.findPrevious("td", align="right").string 
      #match = re.search('\d{2}-\d{2}-\d{4}', postinfo)
      #datePosted = datetime.datetime.strptime(match.group(), '%m-%d-%Y').date()
      #print(datePosted)




   # if stringx.startswith('http://'):   
    #print(a.get('href'))



#print(soup.findAll('a'))




# stringx = ""
# for soup in soup.findAll('a'):   
#    stringx = soup.getText('href')
#    if stringx.startswith('http://'):
#        print(stringx)

#     if stringx.startswith
#    linksarray[counter++]


# print(soup.findAll('a'))
