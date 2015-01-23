__author__ = 'rsukla'

import webbrowser
import time

i = 1
print "When the program is started ", time.ctime()
while i <= 3:

    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=FoNqHH6toDI')
    i = i + 1


