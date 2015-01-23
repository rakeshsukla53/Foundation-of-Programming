__author__ = 'rsukla'

import urllib

def read():

    quotes = open('/home/rsukla/movie_quotes.txt')   #this returns the object of classtype # open returns object type
    contents_of_read = quotes.read()
    output = contents_of_read.split()
    print(output)
    quotes.close()
    profanity(contents_of_read)

# urllib is a library which helps us to import something from the internet

# urlopen is a function

def profanity(text):

    connection = urllib.urlopen("www.wdyl.com/profanity?q="+ text)   #helps to open something from internet
    output = connection.readline()
    print (output)
    connection.close()

read()

