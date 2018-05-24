# -*- coding: utf-8 -*-  
# Author: arlose                                                                                                                                     
# Create：2018/5/18
# 定时上报服务器状态，服务器GPU使用情况，显存剩余情况

import json
import datetime
from ASgpuinfo import queryGPUInfo
import sys
sys.path.append("..")
from database.MSdatabase import AServer
from common import *

configfile = './config.json'

def sendstatus():
    # read config.json 
    jsondata = json.load(file(configfile))
    asname = jsondata['name']
    code = jsondata['code']
    ipaddr = jsondata['ipaddr']
    gpuid = jsondata['gpuid']

    # get the status
    gpumem, gpuusage = queryGPUInfo(gpuid)

    # update the status on the manage server database
    asr = AServer.update(gpuusage=gpuusage,gpumem=gpumem,model="m1",updatetime=datetime.datetime.now()).where(AServer.code==code)
    asr.execute()
    
    return 

if __name__ == "__main__":
    sendstatus()
    print "send analyse server status to manageserver"