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

#585 max page

try:
    connection = mysql.connector.connect(host='localhost',                                         
                                         user='dimitri',
                                         password='dookie92',
                                         database = 'picturesDB')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()   
        #cursor.execute("CREATE TABLE pictureinfo (pictureid VARCHAR(255) PRIMARY KEY, websitename VARCHAR(255), URLstring VARCHAR(255), carmodel VARCHAR(255), cargeneration VARCHAR(255), pictureblob LONGBLOB NOT NULL, picturedate VARCHAR(255), username VARCHAR(255))")     
        sqlStatement = "INSERT INTO pictureinfo (pictureid, websitename, URLstring, carmodel, cargeneration, pictureblob, picturedate, username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        def executeDownload(URLstring):
              try:
                currentphotoID = str(uuid.uuid4())
                imagefile = open(currentphotoID + ".jpg",'wb')
                binaryData = urllib.request.urlopen(URLstring).read()
                print("binary data read successful")
                imagefile.write(binaryData)
                print("binary data write successful")
                imagefile.close()
                print("file save successful")

                postinfo = img.findPrevious('div', class_='message-userContent lbContainer js-lbContainer')['data-lb-caption-desc']
                username = postinfo.split('·', maxsplit=1) 
                datePosted = username[1].split('at',maxsplit=1)  
                print("username found: " + str(username[0]))        
                print("post date found: " + str(datePosted[0]))
                #match = re.search('\d{2}-\d{2}-\d{4}', postinfo)
                #datePosted = datetime.datetime.strptime(match.group(), '%m-%d-%Y').date()  
                currentRecord = (currentphotoID, "7thgenhonda.com", URLstring, "Civic", "7th", binaryData, datePosted[0], username[0])
                cursor.execute(sqlStatement, currentRecord)
                connection.commit()
                print("database commit successful")

              except HTTPError as e:
                print(e)
              else:
                  return 

        
        
        print("made it to the scrape")
        for pagenum in range(583,585):
      
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
            #this if statement filters out all the dead links on the page by comparing url names with valid websites 
            if 'photobucket' in stringx:      
              #print(stringx)
              cleanURL = stringx.split('.', maxsplit=1)
              #print(cleanURL[1])
              genericURL = 'https://www.'
              fullURL = genericURL + cleanURL[1]
              print("this is the full URL found:" + fullURL)
              executeDownload(fullURL)
            elif stringx.startswith("http"):
              executeDownload(stringx)
            #if 'imgur' in stringx:
             # executeDownload()
            #if 'flickr' in stringx and 'static' not in stringx:
             # executeDownload()

        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

