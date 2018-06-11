# -*- coding: utf-8 -*-  
# Author: hsg                                                                                                                                     
# Create：2018/5/28
#服务器注册 @to管理服务器  使用配置文件存储管理服务器信息，通过握手机制将服务器添加到管理服务器数据库中

import json
import datetime

import sys
from CScpuinfo import queryCPUInfo
sys.path.append("..")
from database.MSdatabase import  VServer 
from common import *

configfile = './config.json'

def register():
    # read config.json
    jsondata = json.load(file(configfile))
    csname = jsondata['name']
    cpuid =  jsondata['cpuid']
    code = jsondata['code']
		
    # get the status
    cpumem, cpuusage = queryCPUInfo()
    # register on the manage server database
    try:
	VServer.create(code=code, name=csname, servertype=VSERVER, status=SONLINE, cpumem=cpumem, cpuusage=cpuusage, regtime=datetime.datetime.now(), updatetime=datetime.datetime.now())
    except:
        print str(code)+" is registed"
    return

if __name__ == "__main__":
    register()
    print "register capture server"
