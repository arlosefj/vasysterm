# -*- coding: utf-8 -*-  
# Author: hsg                                                                                                                                     
# Create：2018/5/28
#

import time, threading, os
import json
from CSregister import register
from CScpuinfo import queryCPUInfo, sendstatus
from CSgettaskinfo import gettaskinfo,getcampreset
from CScapture import capture,sendpic

from apscheduler.schedulers.background import BackgroundScheduler  
from apscheduler.schedulers.blocking import BlockingScheduler 

INTERVAL = 120

configfile = './config.json'
jsondata = json.load(file(configfile))
storagepath = jsondata['storageserver']['dir']

#if __name__ == "__main__":
def work():
    print "capture worker"
    #register this worker on manage server
    #register()
    last = time.time()
    curent = last + 121
    #sendstatus()
    newtaskflag = False
    threads = []
    '''
    if(not os.path.exists(storagepath)):
        os.makedirs(storagepath)
        print "mkdir success!\n"
    '''
    while True:
        newcamlist, lasttaskidx = gettaskinfo(1001)
	# send status and get new taskinfo every #INTERVAL seconds
	#curent = time.time()
        if curent - last > INTERVAL:
            last = time.time()
            #sendstatus()
            newcamlist, taskidx = gettaskinfo(1001)
            #print newcamlist
            #print taskidx
            if taskidx != lasttaskidx:
                lasttaskidx = taskidx
                camlist = newcamlist
                newtaskflag = True
            if  newtaskflag:
                pass
                # do something init
            else:
                for i in range(len(newcamlist)):
                    camcode = newcamlist[i][0]
                    camnum = newcamlist[i][1]
                    finalstoragepath = storagepath +'/' + camcode + camnum + "/"
                    if(not os.path.exists(finalstoragepath)):
                        os.makedirs(finalstoragepath)
                        print "mkdir success!\n"
                    else:
                        t = threading.Thread(target=capture,args=(camcode,camnum,finalstoragepath))
                        threads.append(t) 
                for i in range(len(newcamlist)):
                    threads[i].start()
                for i in range(len(newcamlist)):
                    threads[i].join()
                print "task ended!"
        threads =[]
	curent = time.time()
        ##根据任务信息创建多线程进行一定时间间隔的capture，send

if __name__ == "__main__":

    print "start main\n"
    sched = BlockingScheduler()
    sched.add_job(work, 'cron', day_of_week='mon-sun', hour='5-21', minute="*", second="*")#, args=[camcode, camnum, testpath]

    sched.start() 




