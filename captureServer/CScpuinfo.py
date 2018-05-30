# -*- coding: utf-8 -*-  
# Author: hsg                                                                                                                                     
# Create��2018/5/28
#������״̬�ϱ� @to��������� ��ʱ�ϱ�������״̬��������CPUʹ��������ڴ�ʣ�����

#������psutil��:pip install psutil

import psutil
import os,datetime,time

def queryCPUInfo(cpuid):
		try:	
	    data = psutil.virtual_memory()
	    total = data.total #���ڴ�,��λΪbyte
	    free = data.available #�����ڴ�
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
   