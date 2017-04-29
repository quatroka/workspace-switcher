#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Setup file to workspace-switch """
import os
from shutil import copy

ROOT_DIR = os.environ['HOME'] + '/.workspace-switcher'
os.system('mkdir ' + ROOT_DIR)

# Copy script file
copy('run.py', ROOT_DIR)

# Make a executable file
os.system('chmod 755 ' + ROOT_DIR + '/run.py')
