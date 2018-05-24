# -*- coding: utf-8 -*-  
# Author: arlose                                                                                                                                     
# Create：2018/5/18
# 服务器GPU使用情况，显存剩余情况
from pynvml import *
# sudo pip install nvidia-ml-py

def queryGPUInfo(gpuid):
    try:
        nvmlInit()
        # TODO multi gpu info like below
        # num = nvmlDeviceGetCount()
        # print num
        # for i in range(num):
        #     handle = nvmlDeviceGetHandleByIndex(i)
        #     info = nvmlDeviceGetMemoryInfo(handle)                                                                                                   
        #     temp = nvmlDeviceGetTemperature(handle, 0)
        #     perc = nvmlDeviceGetFanSpeed(handle)
        #     power = nvmlDeviceGetPowerUsage(handle)
        #     util = nvmlDeviceGetUtilizationRates(handle)
        #     print "Device:", nvmlDeviceGetName(handle),  str(temp)+"C"
        #     print "Total memory:", info.total/1000000
        #     print "Used memory:", info.used/1000000
        #     print str(perc)+"%"
        #     print str(power/1000)+"W"
        #     print util.gpu, util.memory
        info = ""
        handle = nvmlDeviceGetHandleByIndex(gpuid)
        name = nvmlDeviceGetName(handle)
        mem = nvmlDeviceGetMemoryInfo(handle)
        temp = nvmlDeviceGetTemperature(handle, 0)
        #perc = nvmlDeviceGetFanSpeed(handle)
        #power = nvmlDeviceGetPowerUsage(handle)
        util = nvmlDeviceGetUtilizationRates(handle)
        memuse = mem.used*1.0/mem.total 
        memunused = mem.total/1000000 - mem.used/1000000
        # info = name + ": Mem: " + str(mem.used/1000000)+ "/"+ str(mem.total/1000000)+ " Temp: " + str(temp)+"C Util: " + str(util.gpu) 
        info = str(mem.used/1000000)+ "/"+ str(mem.total/1000000)
        gpuused = util.gpu
    except:
        info = "no gpu found"
        gpuused = 0
    return info, gpuused

if __name__ == "__main__":
    info, gpuused = queryGPUInfo(0)
    print info
    print gpuused