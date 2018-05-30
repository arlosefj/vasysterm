# -*- coding: utf-8 -*-  
# Author: hsg                                                                                                                                     
# Create：2018/5/28
#服务器注册 @to管理服务器  使用配置文件存储管理服务器信息，通过握手机制将服务器添加到管理服务器数据库中

import json
import datetime

import sys
sys.path.append("..")
from database.MSdatabase import AServer, SServer 
from common import *

configfile = './config.json'

def register():
		# read config.json
		jsondata = json.load(file(configfile))
		csname = jsondata['name']
		cpuid =  jsondata['cpuid']
		code = jsondata['code']
		
		
		# get the status
		cpumem, cpuusage = queryCPUInfo(cpuid)
		
		# register on the manage server database
		try:
				AServer.create(name=csname,servertype=CSERVER,status=SONLINE, cpuusage=cpuusage,cpumem=cpumem,model="",regtime=datetime.datetime.now(), updatetime=datetime.datetime.now())
		except:
				print str(code)+" is registed"
		return

if __name__ == "__main__":
    register()
    print "register capture server"