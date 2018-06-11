# -*- coding: utf-8 -*-  
# Author: arlose                                                                                                                                     
# Create：2018/5/18
import datetime
from MSdatabase import *

if __name__ == "__main__":
    # User.create(name="test", passwd="test123", email="test@qq.com", mobile="1234567890", authority=1, 
    #    regIP="192.168.0.111", regtime=datetime.datetime.now(), lastloginIP="192.168.0.111", lastlogintime=datetime.datetime.now())
    # Platform.create(code="12345678", ipaddr="192.168.0.101", port=7000, loginname="admin", loginpwd="admin", description="platform1", regtime=datetime.datetime.now())
    SingleCamera.create(code=9001, name="singlecam1", ip="192.168.0.201", camtype=1, status=1, regtime=datetime.datetime.now(), updatetime=datetime.datetime.now())
    # VServer.create(code=1001,name="videoparser1", servertype=1,status=1,ipaddr="192.168.0.102",cpu=30,memery="1000/8000", regtime=datetime.datetime.now())
    # SServer.create(code=2001,name="storage1",servertype=1,status=1,ipaddr="192.168.0.103",harddisk="10/10000",regtime=datetime.datetime.now())
    # TServer.create(code=3001,name="training1",servertype=2,status=1,ipaddr="192.168.0.104",gpuusage=10,gpumem="2000/10000",regtime=datetime.datetime.now())
    # AServer.create(code=4001,name="analyse1",servertype=2,status=1,ipaddr="192.168.0.105",gpuusage=10,gpumem="2000/10000",model="8001,8002",regtime=datetime.datetime.now())
    CamPreset.create(camcode=9001,preset="{\"length\":1,\"Preset_1\":[{\"Type\":\"0\",\"Points\":\"0.28 0.15;0.34 0.12;0.79 0.72;0.79 0.81;0.48 0.9\"},{\"Type\":\"0 1\",\"Points\":\"0.17 0.18;0.24 0.03;0.78 0.79;0.68 0.8\"}]}",lasttime=datetime.datetime.now())
    CamPreset.create(camcode=1234,preset="{\"length\":0,\"Type\":\"0 1\"}",lasttime=datetime.datetime.now())
    VTask.create(code=1001,idx=1,camlist="1000007,8; 1000089,4; 1000095,0; 1000099,0; 1000104,0; 1000107,0; 1000109,0",lasttime=datetime.datetime.now())
   # VTask.create(code=1002,idx=2,camlist="1000093",lasttime=datetime.datetime.now())
    ATask.create(code=4003,camlist="9001,mobile; 1234, dahua1",lasttime=datetime.datetime.now())
    TModel.create(code=8001,description="model1",modelpath="/myShare/model/model1.bin",regtime=datetime.datetime.now())
    TModel.create(code=8002,description="model2",modelpath="/myShare/model/model2.bin",regtime=datetime.datetime.now())
    Event.create(camcode=9001,etype=1,imagepath="/myShare/data/event/test1.jpg",sendtime=datetime.datetime.now()) 
