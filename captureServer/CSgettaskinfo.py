# -*- coding: utf-8 -*-  
# Author: hsg                                                                                                                                     
# Create：2018/5/28
#
# 登陆平台
#        调用大华linux SDK登陆监控平台
# 获取配置信息 @from管理服务器
#        读取管理服务器数据库中 #解码任务信息，解析其中相机编码列表
# 获取码流
#        根据上面获得的相机编码列表，调用大华linux SDK获取每个相机rtsp码流地址

import os
import sys
sys.path.append("..")
from database.MSdatabase import AServer, SServer 
from common import *

#登录大华平台，根据相机列表，获取每个相机的rtsp码流地址
def login():
		#add code here
		pass			
		return
		
# 获取解码任务信息
def gettaskinfo():
		t = VTask.get(VTask.code == code)
		tmplist = t.camlist.encode('ascii').split(';')
		camlist = []
		for string in tmplist:
        camcode, platform = string.strip().split(',')
        camlist.append((camcode.strip(), platform.strip()))
    return camlist, t.id

#获取相机预置位信息
def getcampreset(camcode):
		#部分数据库操作还需要询问冯老师
		pass
		return

if __name__ == "__main__":
		print "cs gettaskinfo"
		#CSgettaskinfo
		camlist, tid = gettaskinfo()
    print tid
    print camlist
	  
