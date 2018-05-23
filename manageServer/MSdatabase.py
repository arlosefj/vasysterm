# -*- coding: utf-8 -*-  
# Author: arlose                                                                                                                                     
# Create：2018/5/18
from peewee import *

db = MySQLDatabase("vasystem", host="127.0.0.1", user="root", passwd="knowvision")
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

#用户信息
# id（主键），用户名（唯一），加密用户密码，用户邮箱，用户手机号码，用户属性（权限），用户注册时间，用户注册IP，上一次登陆时间，上一次登陆IP
class User(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(unique=True)
    passwd = CharField()
    email = CharField(unique=True)
    mobile = CharField(unique=True)
    authority = IntegerField()
    regIP = CharField()
    regtime = DateTimeField()
    lastloginIP = CharField()
    lastlogintime = DateTimeField()

#平台信息
# id（主键），平台编码（唯一，自动生成），平台IP地址，平台登陆端口，平台登陆用户名，加密平台登陆密码， 平台描述，平台加入时间
class Platform(BaseModel):
    id = IntegerField(primary_key=True)
    code = CharField(unique=True)
    ipaddr = CharField()
    port = IntegerField()
    loginname = CharField()
    loginpwd = CharField()
    description = CharField()
    regtime = DateTimeField()

#非平台相机设备信息
# id（主键），相机编码（唯一，自动生成），相机名称，相机IP，相机类型，相机加入时间，相机状态
class SingleCamera(BaseModel):
    id = IntegerField(primary_key=True)
    code = IntegerField(unique=True)
    name = CharField()
    ip = CharField()
    camtype = IntegerField()
    status = IntegerField()
    regtime = DateTimeField()

#解码服务器信息
# id（主键），服务器编码（唯一，自动生成），服务器名称，服务器类型，服务器状态，服务器IP，服务器资源情况（CPU占用率，内存占用率），服务器加入系统时间
class VServer(BaseModel):
    id = IntegerField(primary_key=True)
    code = IntegerField(unique=True)
    name = CharField()
    servertype = IntegerField()
    status = IntegerField()
    ipaddr = CharField()
    cpu = IntegerField()
    memery = CharField()
    regtime = DateTimeField()

#存储服务器信息
# id（主键），服务器编码（唯一，自动生成），服务器名称，服务器类型，服务器状态，服务器IP，服务器资源情况（硬盘剩余情况），服务器加入系统时间
class SServer(BaseModel):
    id = IntegerField(primary_key=True)
    code = IntegerField(unique=True)
    name = CharField()
    servertype = IntegerField()
    status = IntegerField()
    ipaddr = CharField()
    harddisk = CharField()
    regtime = DateTimeField()

#训练服务器信息
# id（主键），服务器编码（唯一，自动生成），服务器名称，服务器类型，服务器状态，服务器IP，服务器资源情况（GPU占用率，显存剩余情况），服务器加入系统时间
class TServer(BaseModel):
    id = IntegerField(primary_key=True)
    code = IntegerField(unique=True)
    name = CharField()
    servertype = IntegerField()
    status = IntegerField()
    ipaddr = CharField()
    gpuusage = IntegerField()
    gpumem = CharField()
    regtime = DateTimeField()

#分析服务器信息
# id（主键），服务器编码（唯一，自动生成），服务器名称，服务器类型，服务器状态，服务器IP，服务器资源情况（GPU占用率，显存剩余情况），训练模型列表，服务器加入系统时间
class AServer(BaseModel):
    id = IntegerField(primary_key=True)
    code = IntegerField(unique=True)
    name = CharField()
    servertype = IntegerField()
    status = IntegerField()
    ipaddr = CharField()
    gpuusage = IntegerField()
    gpumem = CharField()
    model = CharField()
    regtime = DateTimeField()

#相机预置位信息
# id（主键），相机编码（唯一），预置位信息描述（json字符串，参考配置数据 #预置位电子围栏格式），最后一次配置更新时间
class CamPreset(BaseModel):
    id = IntegerField(primary_key=True)
    camcode = IntegerField(unique=True)
    preset = TextField()
    lasttime = DateTimeField()

#解码任务信息
# id（主键），服务器编码（唯一，与解码服务器对应），相机编码列表（如果是平台下的相机需要加上平台编码，如 平台编码_相机编码），任务编号，最后一次任务更新时间
class VTask(BaseModel):
    id = IntegerField(primary_key=True)
    code = IntegerField(unique=True)
    idx = IntegerField()
    camlist = TextField()
    lasttime = DateTimeField()

#分析任务信息
# id（主键），服务器编码（唯一，与分析服务器对应），相机编码列表（如果是平台下的相机需要加上平台编码，如 平台编码_相机编码），任务编号，最后一次任务更新时间
class ATask(BaseModel):
    id = IntegerField(primary_key=True)
    code = IntegerField(unique=True)
    idx = IntegerField()
    camlist = TextField()
    lasttime = DateTimeField()

#训练模型信息
# id（主键），训练模型编码（唯一），模型描述，模型位置，加入系统时间
class TModel(BaseModel):
    id = IntegerField(primary_key=True)
    code = IntegerField(unique=True)
    description = CharField()
    modelpath = TextField()    
    regtime = DateTimeField()

#上报事件信息
# id（主键，唯一），相机编码，事件类型，上报时间，存储图片地址
class Event(BaseModel):
    id = IntegerField(primary_key=True)
    camcode = IntegerField()
    etype = IntegerField()
    imagepath = TextField()
    sendtime = DateTimeField()
