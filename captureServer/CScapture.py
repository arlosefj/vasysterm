# -*- coding: utf-8 -*-  
# Author: hsg                                                                                                                                     
# Create：2018/5/28
#解析码流为图片
#    使用ffmpeg解析rtsp码流，隔一定时间（如10秒，可配置）保存一张图片，图片命名格式为：当前预置位编号_时间.jpg  解析码流图片命名中的当前预置位编号应与云台控制相一致。​
#上传图片到存储服务器 @to存储服务器
#    将图片上传到存储服务器对应文件夹中，一般采用 ～/data/平台编码/相机编码/ 文件夹


import time, os ,datetime,json
from CSregister import register
from CScpuinfo import queryCPUInfo
from CSgettaskinfo import gettaskinfo,getcampreset

configfile = './config.json'
jsondata = json.load(file(configfile))
commandcode = jsondata['commandcode']

#解析码流为图片
def capture(camcode,camnum,path):#campreset resevered
    try:
        time_local = time.localtime()
        #转换成新的时间格式(2016-05-09 18:59:20)
	strtime = time.strftime("%Y%m%d%H%M%S",time_local)
	#获取预置位编号和时间，给图片取名字 名字根据时间等给定
	picname = path + camcode + "%24" + camnum + "_" + strtime + ".jpg"
	str = commandcode + camcode + "%24" + camnum + "&substream=1\" " + picname
	os.system(str)
    except:
	print "capture failed"
    return

#上传图片到存储服务器 @to存储服务器 需要询问杨师兄上传接口
def sendpic(picid):
    try:
        #do something here
        pass
    except:
        print "send pic failed"
    return
		
if __name__ == "__main__":
    camcode = "1000091"
    camnum = "0"
    testpath = "./"
    capture(camcode,camnum,testpath)#可以拿来测试
    #sendpic(picid)
    print "capture process"
	
