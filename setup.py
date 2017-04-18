""" Setup file to workspace-switch """
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

HOME_DIR = os.environ['HOME']
os.system('mkdir ' + HOME_DIR + '/.workspace-switch')
FILE = open(HOME_DIR + '/.workspace-switch/workspaces', 'w')
FILE.write('0')
FILE.close()
