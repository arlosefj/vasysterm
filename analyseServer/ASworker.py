# -*- coding: utf-8 -*-  
# Author: arlose                                                                                                                                     
# Create：2018/5/18
import time
from ASregister import register
from ASstatus import sendstatus
from ASanalyse import gettaskinfo, getimage, analyse

INTERVAL = 30

if __name__ == "__main__":
    print "analyse worker"
    # register this worker on manage server
    register()
    last = time.time()
    camlist, lasttaskidx = gettaskinfo()
    sendstatus()
    newtaskflag = True
    while True:
        # send status and get new taskinfo every #INTERVAL seconds
        curent = time.time()
        if curent - last > INTERVAL:
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
            if imagepath is not None:
                analyse(imagepath, imageinfo)
