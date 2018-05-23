# coding: utf-8
import time
from ASregister import register
from ASstatus import sendstatus
from ASanalyse import *

SENDINTERVAL = 10000

if __name__ == "__main__":
    print "analyse worker"
    # register this worker on manage server
    register()
    last = time.time()
    lasttaskidx = -1
    camlist, lasttaskidx = gettaskinfo()
    sendstatus()
    newtaskflag = True
    while True:
        # send status and get new taskinfo interval
        curent = time.time()
        if curent - last > SENDINTERVAL:
            last = time.time()
            sendstatus()
            newcamlist, taskidx = gettaskinfo()
            if taskidx != lasttaskidx:
                lasttaskidx = taskidx
                camlist = newcamlist
                newtaskflag = True

        # analyse
        if newtaskflag:
            # do something init
            newtaskflag = False
        for camcode in camlist:
            imagepath, imageinfo = getimage(camcode)
            analyse(imagepath, imageinfo)
