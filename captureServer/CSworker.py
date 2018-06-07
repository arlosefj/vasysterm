# -*- coding: utf-8 -*-  
# Author: hsg                                                                                                                                     
# Create：2018/5/28
#

import time, threading
from CSregister import register
from CScpuinfo import queryCPUInfo, sendstatus
from CSgettaskinfo import gettaskinfo,getcampreset
from CScapture import capture,sendpic

INTERVAL = 3000

if __name__ == "__main__":
    print "capture worker"
    #register this worker on manage server
    #register()
    last = time.time()
    #sendstatus()
    newtaskflag = False
    threads = []
	while True:
        newcamlist, lasttaskidx = gettaskinfo(1001)
		# send status and get new taskinfo every #INTERVAL seconds
		curent = time.time()
        if curent - last > INTERVAL:
            last = time.time()
            #sendstatus()
            newcamlist, taskidx = gettaskinfo(1001)
            print newcamlist
            print taskidx
            if taskidx != lasttaskidx:
                lasttaskidx = taskidx
                camlist = newcamlist
                newtaskflag = True
        if  newtaskflag:
            # do something init
        else:
            for i in range(len(newcamlist)-1):
                camcode = newcamlist[i][0]
                camnum = newcamlist[i][1]
                t = threading.Thread(target=capture,args=(camcode,camnum))
                threads.append(t) 
            for i in range(len(newcamlist)-1):
                threads[i].start()
            for i in range(len(newcamlist)-1):
                threads[i].join()
            print "task ended!"
        threads =[]
        ##根据任务信息创建多线程进行一定时间间隔的capture，send
        