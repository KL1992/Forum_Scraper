import urllib
import urllib.request
import re, datetime
import _string
import sqlite3
from urllib.request import Request
from bs4 import BeautifulSoup

#1170 max page

conn = sqlite3.connect('pictures.db')
c = conn.cursor()
#c.execute("""CREATE TABLE picturedata (
#  picturepath text,
#  cartype text,
#  postinfo text, 
#  imageblob blob
#  )""")
conn.commit()
conn.close()


#this for loop iterates over each forum page, the indicies from the loop feed into theurl string
for pagenum in range(1003,1004):
  
  #each url will need tailoring since each forum formats their pages differently
  theurl = "https://www.7thgenhonda.com/forum/printthread.php?t=44&pp=10&page=" + str(pagenum)
  #below are the soup calls to open the webpage and spoof any anti-botting hurdles
  theheader = {'User-Agent': 'Mozilla/5.0'}
  req = Request(theurl, headers = theheader)
  thepage = urllib.request.urlopen(req)
  soup = BeautifulSoup(thepage,"html.parser")  

  #this for loop goes through the webpage and parses out each element and finds the picture links
  for a in soup.findAll('a'):
    stringx = a.get('href')
    #this if statement filters out all the dead links on the page by comparing url names with valid websites 
    if 'photobucket' in stringx or 'flickr' in stringx:              
      print(stringx)
      postinfo = a.findPrevious("td", align="right").string 
      match = re.search('\d{2}-\d{2}-\d{4}', postinfo)
      datePosted = datetime.datetime.strptime(match.group(), '%m-%d-%Y').date()
      print(datePosted)




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
