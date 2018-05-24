# -*- coding: utf-8 -*-  
# Author: arlose                                                                                                                                     
# Create：2018/5/18
# 使用配置文件存储管理服务器信息，通过握手机制将服务器添加到管理服务器数据库中
import json
import datetime
from ASgpuinfo import queryGPUInfo
import sys
sys.path.append("..")
from database.MSdatabase import AServer
from common import *

configfile = './config.json'

def register():
    # read config.json 
    jsondata = json.load(file(configfile))
    asname = jsondata['name']
    code = jsondata['code']
    ipaddr = jsondata['ipaddr']
    gpuid = jsondata['gpuid']

    # get the status 
    gpumem, gpuusage = queryGPUInfo(gpuid)

    # register on the manage server database
    try:
        AServer.create(code=code,name=asname,servertype=ASERVER,status=SONLINE,ipaddr=ipaddr,gpuusage=gpuusage,gpumem=gpumem,model="",regtime=datetime.datetime.now(), updatetime=datetime.datetime.now())
    except:
        print str(code)+" is registed"
    return

if __name__ == "__main__":
    register()
    print "register analyse server"