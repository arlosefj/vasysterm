# -*- coding: utf-8 -*-  
# Author: arlose                                                                                                                                     
# Create：2018/5/18
from peewee import *
from MSdatabase import *

def createTable():
    User.create_table()
    Platform.create_table()
    SingleCamera.create_table()
    VServer.create_table()
    SServer.create_table()
    TServer.create_table()
    AServer.create_table()
    CamPreset.create_table()
    VTask.create_table()
    ATask.create_table()
    TModel.create_table()
    Event.create_table()
    return 

if __name__ == "__main__":
    createTable()