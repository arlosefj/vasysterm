# -*- coding: utf-8 -*-  
# Author: hsg                                                                                                                                     
# Create：2018/5/28
#

import time, threading
from CSregister import register
from CScpuinfo import queryCPUInfo, sendstatus
from CSgettaskinfo import gettaskinfo,getcampreset

INTERVAL = 30

if __name__ == "__main__":
		print "capture worker"
		# register this worker on manage server
		register()
		last = time.time()
		sendstatus()
		newtaskflag = False
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
        
        #根据任务信息创建多线程进行一定时间间隔的capture，send
        #do something here        