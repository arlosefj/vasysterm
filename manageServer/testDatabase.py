# -*- coding: utf-8 -*-  
# Author: arlose                                                                                                                                     
# Create：2018/5/18
import datetime
from MSdatabase import *

if __name__ == "__main__":
    User.create(id=1, name="test", passwd="test123", email="test@qq.com", mobile="1234567890", authority=1, 
        regIP="192.168.0.111", regtime=datetime.datetime.now(), lastloginIP="192.168.0.111", lastlogintime=datetime.datetime.now())
    # Platform.create(id=1,code="12345678", ipaddr="192.168.0.101", port=7000, loginname="admin", loginpwd="admin", description="platform1", regtime=datetime.datetime.now())
    # SingleCamera.create(id=1,code=9001, name="singlecam1", ip="192.168.0.201", camtype=1, status=1, regtime=datetime.datetime.now())
    # VServer.create(id=1,code=1001,name="videoparser1", servertype=1,status=1,ipaddr="192.168.0.102",cpu=30,memery="1000/8000", regtime=datetime.datetime.now())
    # SServer.create(id=1,code=2001,name="storage1",servertype=1,status=1,ipaddr="192.168.0.103",harddisk="10/10000",regtime=datetime.datetime.now())
    # TServer.create(id=1,code=3001,name="training1",servertype=2,status=1,ipaddr="192.168.0.104",gpuusage=10,gpumem="2000/10000",regtime=datetime.datetime.now())
    # AServer.create(id=1,code=4001,name="analyse1",servertype=2,status=1,ipaddr="192.168.0.105",gpuusage=10,gpumem="2000/10000",model="8001,8002",regtime=datetime.datetime.now())
    # CamPreset.create(id=1,camcode=9001,preset="{\"length\":0}",lasttime=datetime.datetime.now())
    # VTask.create(id=1,code=1001,idx=1,camlist="9001",lasttime=datetime.datetime.now())
    # ATask.create(id=1,code=4001,idx=1,camlist="9001",lasttime=datetime.datetime.now())
    # TModel.create(id=1,code=8001,description="model1",modelpath="/home/knowvision/model/model1.bin",regtime=datetime.datetime.now())
    # TModel.create(id=2,code=8002,description="model2",modelpath="/home/knowvision/model/model2.bin",regtime=datetime.datetime.now())
    # Event.create(id=1,camcode=9001,etype=1,imagepath="/home/knowvision/data/test1.jpg",sendtime=datetime.datetime.now())
