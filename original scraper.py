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
for pagenum in range(582,583):
  
  #each url will need tailoring since each forum formats their pages differently
  theurl = "https://www.7thgenhonda.com/forum/printthread.php?t=44&pp=10&page=" + str(pagenum)
  #below are the soup calls to open the webpage and spoof any anti-botting hurdles
  theheader = {'User-Agent': 'Mozilla/5.0'}
  req = Request(theurl, headers = theheader)
  thepage = urllib.request.urlopen(req)
  soup = BeautifulSoup(thepage,"html.parser")  

  #this for loop goes through the webpage and parses out each element and finds the picture links
  for a in soup.findAll('a'):
    stringx = str(a.get('href'))
    #this if statement filters out all the dead links on the page by comparing url names with valid websites 
    if 'photobucket' in stringx:      
        #print(stringx)
        cleanURL = stringx.split('.', maxsplit=1)
        #print(cleanURL[1])
        genericURL = 'https://www.'
        fullURL = genericURL + cleanURL[1]
        print(fullURL)
        postinfo = a.findPrevious('time')['data-date-string']
        print(str(postinfo)) 
   


    #try:
    #  imagefile = open(str(uuid.uuid4()) + ".jpg",'wb')
    #  imagefile.write(urllib.request.urlopen(fullURL).read())
    #  imagefile.close()
   # except HTTPError as e:
   #   print(e)
  #  else:
 #         break 


    #postinfo = a.findPrevious('time')
    #print(str(postinfo))   
    #match = re.search('\d{2}-\d{2}-\d{4}', postinfo)
    #print(match)
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
