# -*- coding: utf-8 -*-  
# Author: hsg                                                                                                                                     
# Create��2018/5/28
#
# ��½ƽ̨
#        ���ô�linux SDK��½���ƽ̨
# ��ȡ������Ϣ @from���������
#        ��ȡ������������ݿ��� #����������Ϣ������������������б�
# ��ȡ����
#        ���������õ���������б����ô�linux SDK��ȡÿ�����rtsp������ַ

import os
import sys
sys.path.append("..")
from database.MSdatabase import AServer, SServer 
from common import *

#��¼��ƽ̨����������б���ȡÿ�������rtsp������ַ
def login():
		#add code here
		pass			
		return
		
# ��ȡ����������Ϣ
def gettaskinfo():
		t = VTask.get(VTask.code == code)
		tmplist = t.camlist.encode('ascii').split(';')
		camlist = []
		for string in tmplist:
        camcode, platform = string.strip().split(',')
        camlist.append((camcode.strip(), platform.strip()))
    return camlist, t.id

#��ȡ���Ԥ��λ��Ϣ
def getcampreset(camcode):
		#�������ݿ��������Ҫѯ�ʷ���ʦ
		pass
		return

if __name__ == "__main__":
		print "cs gettaskinfo"
		#CSgettaskinfo
		camlist, tid = gettaskinfo()
    print tid
    print camlist
	  
