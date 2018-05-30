# -*- coding: utf-8 -*-  
# Author: hsg                                                                                                                                     
# Create：2018/5/28
#解析码流为图片
#    使用ffmpeg解析rtsp码流，隔一定时间（如10秒，可配置）保存一张图片，图片命名格式为：当前预置位编号_时间.jpg  解析码流图片命名中的当前预置位编号应与云台控制相一致。​
#上传图片到存储服务器 @to存储服务器
#    将图片上传到存储服务器对应文件夹中，一般采用 ～/data/平台编码/相机编码/ 文件夹


import time 
from CSregister import register
from CScpuinfo import queryCPUInfo
from CSgettaskinfo import gettaskinfo,getcampreset

#解析码流为图片
def capture(camcode,campreset)
		try:
			#获取预置位编号和时间，给图片取名字
			pass
		except:
			print "capture failed"
		return

#上传图片到存储服务器 @to存储服务器
def sendpic(picid)
		try:
			#do something here
			pass
		except:
			print "send pic failed"
		return
		
if __name__ == "__main__":
	print "capture process"
	