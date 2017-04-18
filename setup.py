#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Setup file to workspace-switch """
import os
from shutil import copy

ROOT_DIR = os.environ['HOME'] + '/.workspace-switcher'
os.system('mkdir ' + ROOT_DIR)

# Create workspace file
FILE = open(ROOT_DIR + '/workspaces', 'w')
FILE.write('0')
FILE.close()

# Copy script file
copy('run.py', ROOT_DIR)

# Make a executable file
os.system('chmod 755 ' + ROOT_DIR + '/run.py')
