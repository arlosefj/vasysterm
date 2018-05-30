# -*- coding: utf-8 -*-  
# Author: hsg                                                                                                                                     
# Create：2018/5/28
#服务器状态上报 @to管理服务器 定时上报服务器状态，服务器CPU使用情况，内存剩余情况

#先下载psutil库:pip install psutil

import psutil
import os,datetime,time

def 	queryCPUInfo(cpuid):
		try:	
	    	data = psutil.virtual_memory()
	      total = data.total #总内存,单位为byte
	      free = data.available #可用内存
	      cpumem =  "Memory usage:%d"%(int(round(data.percent)))+"%"+"  "
	      cpuusage = "CPU:%0.2f"%psutil.cpu_percent(interval=1)+"%"
	  except:
	  		info = "no cpu found"
	  return cpumem,cpuusage

def sendstatus():
    # read config.json 
    jsondata = json.load(file(configfile))
    asname = jsondata['name']
    code = jsondata['code']
		cpuid =  jsondata['cpuid']
		
    # get the status
    cpumem, cpuusage = queryCPUInfo(gpuid)

    # update the status on the manage server database
    asr = CServer.update(cpuusage=cpuusage,cpumem=cpumem,updatetime=datetime.datetime.now()).where(AServer.code==code)
    asr.execute()   
    return 
    
if  __name__=="__main__":
		info = queryCPUInfo()
    print info+"\b"*(len(info)+1)
   