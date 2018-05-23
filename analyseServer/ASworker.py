# coding: utf-8
from ASregister import register
from ASstatus import sendstatus
from ASanalyse import *

if __name__ == "__main__":
    print "analyse worker"
    # register this worker on manage server
    register()
    # while True:
        # add time