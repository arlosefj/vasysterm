# -*- coding: utf-8 -*-  
# Author: arlose                                                                                                                                     
# Create：2018/5/18
'''
获取配置信息 @from管理服务器
    读取管理服务器数据库中分析任务信息，解析其中相机编码列表
获取待分析图片 @from存储服务器
    根据上面获得的相机编码列表依次从存储服务器中获取相应图片
根据模型检测图片内容
    根据任务类型进行深度学习前向推理检测，得到检测物体框
分析策略
    根据配置文件分析类型和检测结果分析城管相关业务
结果上报 @to存储服务器 @to管理服务器
    结果图片上传到存储服务器，结果内容添加到管理服务器上报事件信息数据库中
'''
import json
import datetime
import time
import sys
sys.path.append("..")
from database.MSdatabase import AServer, ATask, CamPreset, Event
from common import *

configfile = './config.json'
jsondata = json.load(file(configfile))
asname = jsondata['name']
code = jsondata['code']
ipaddr = jsondata['ipaddr']
gpuid = jsondata['gpuid']
localdir = jsondata['localdir']
storageip = jsondata['storageserver']['ip']
storagepath = jsondata['storageserver']['dir']

def gettaskinfo():
    t = ATask.get(ATask.code == code)
    tmplist = t.camlist.encode('ascii').split(';')
    camlist = []
    for string in tmplist:
        camcode, platform = string.strip().split(',')
        camlist.append((camcode.strip(), platform.strip()))
    return camlist, t.id

def getcamcfg(camlist):
    cfglist = {}
    for code, _ in camlist:
        try:
            p = CamPreset.get(CamPreset.camcode==code)
            cfglist[code] = p.preset
        except CamPreset.DoesNotExist:
            cfglist[code] = NOPRESET
    return cfglist

# TODO find the oldest image file in the folder
def getimage(camcode, platform):
    camimgdir = localdir+platform+'/'+camcode
    camimgpath = camimgdir+'/1_20180524100000.jpg'
    return camimgpath

# {"Presets":[{"Perset_1":[{"Type":"0 1","Points":"0.28 0.15;0.34 0.12;0.79 0.72;0.79 0.81;0.48 0.9"},{"Type":"1","Points":"0.17 0.18;0.24 0.03;0.78 0.79;0.68 0.8"}]}]}{"Presets":[{"Perset_1":[{"Type":"0 1","RegionID":"0","Points":"0.28 0.15;0.34 0.12;0.79 0.72;0.79 0.81;0.48 0.90"}]}]}
def getpreset(camimgpath):
    presetidx = int(camimgpath.split('/')[-1].split('_')[0])
    #presetstr = "Preset_"+str(presetidx)
    #tasktype = json.loads(camcfg)['Presets'][presetstr]
    return presetidx

def getdettypespreset(presetcfg):
    types = []
    for cfg in presetcfg:
        tmplist = cfg['Type'].encode('ascii').split(' ')
        for tmp in tmplist:
            if tmp not in types:
                types.append(tmp)
    return types

def detectimgWT(camimgpath):
    boxs = "0 0; 1 0; 1 1; 0 1"
    return boxs

def detectimgDWD(camimgpath):
    boxs = "0 0; 1 0; 1 1; 0 1"
    return boxs

def detectimgLDTF(camimgpath):
    boxs = "0 0; 1 0; 1 1; 0 1"
    return boxs

def analyse(camcode, camimgpath, camcfg):    
    print camcode
    print camimgpath
    print camcfg
    # get tasktype from presetinfo
    jsoncfg = json.loads(camcfg)
    length = jsoncfg['length']
    detecttypes = []
    if(length>0):
        presetidx = getpreset(camimgpath)
        presetstr = "Preset_"+str(presetidx)
        presetcfg = jsoncfg[presetstr]
        detecttypes = getdettypespreset(presetcfg)
    else:
        tmplist = jsoncfg['Type'].encode('ascii').split(' ')
        for tmp in tmplist:
            if tmp not in detecttypes:
                detecttypes.append(tmp)

    print detecttypes
    # detect image and strategy
    if WT in detecttypes:
        detectimgWT(camimgpath)
        print "detect WT"
    if DWD in detecttypes:
        detectimgDWD(camimgpath)
        print "detect DWD"
    if LDTF in detecttypes:
        detectimgLDTF(camimgpath)
        print "detect LDTF"

    time.sleep(10)

    # strategy
    # every region has its own strategy

    # upsend the result
    Event.create(camcode=camcode,etype=EWT,imagepath="/myShare/data/event/test.jpg",sendtime=datetime.datetime.now())

    return

if __name__ == "__main__":
    print "analyse task"
    # gettaskinfo
    camlist, tid = gettaskinfo()
    print tid
    print camlist
    print type(camlist)

    # getcamcfg
    cfglist = getcamcfg(camlist)
    print cfglist

    # getimg
    imgpath = getimage(camlist[0][0], camlist[0][1])
    print imgpath

    # get preset idx
    presetidx = getpreset(imgpath)
    print presetidx

    # get presetcfg
    presetstr = "Preset_"+str(presetidx)
    camcfg = cfglist[camlist[0][0]].encode('ascii')
    print camcfg
    print type(camcfg)
    jsonda = json.loads(camcfg)
    print '##############'
    print jsonda
    presetcfg = jsonda[presetstr]
    print presetcfg
    print type(presetcfg)


