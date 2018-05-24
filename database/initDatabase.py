# -*- coding: utf-8 -*-  
# Author: arlose                                                                                                                                     
# Create：2018/5/18
from peewee import *
from MSdatabase import *

def createTable():
    User.drop_table()
    User.create_table()
    Platform.drop_table()
    Platform.create_table()
    SingleCamera.drop_table()
    SingleCamera.create_table()
    VServer.drop_table()
    VServer.create_table()
    SServer.drop_table()
    SServer.create_table()
    TServer.drop_table()
    TServer.create_table()
    AServer.drop_table()
    AServer.create_table()
    CamPreset.drop_table()
    CamPreset.create_table()
    VTask.drop_table()
    VTask.create_table()
    ATask.drop_table()
    ATask.create_table()
    TModel.drop_table()
    TModel.create_table()
    Event.drop_table()
    Event.create_table()
    return 

if __name__ == "__main__":
    createTable()