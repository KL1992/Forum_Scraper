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
        #cursor.execute("CREATE TABLE pictureinfo (pictureid VARCHAR(255) PRIMARY KEY,\
        #    websitename VARCHAR(255), URLstring VARCHAR(255), carmodel VARCHAR(255),\
        #        cargeneration VARCHAR(255), pictureblob LONGBLOB NOT NULL, picturedate VARCHAR(255),\
        #             username VARCHAR(255))")            

        sqlStatement = "INSERT INTO pictureinfo (pictureid, websitename, URLstring, carmodel, cargeneration, pictureblob, picturedate, username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        currentRecord = ("currentphotoID", "7thgenhonda.com", "fullURL", "Civic", "7th", "pictureblob", "datePosted[0]", "username[0]")
        #cursor.execute("select database();")
        cursor.execute(sqlStatement, currentRecord)
        connection.commit()
        print("database commit successful")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

