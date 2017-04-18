""" This file execute de switch betten workspaces. """
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from subprocess import run
import os

HOME_DIR = os.environ['HOME']
FILE = open(HOME_DIR + '/.workspaces', 'r')

EXEC = 'xdotool get_desktop'

if int(FILE.read()) == 0:
    EXEC = 'xdotool set_desktop 1'
    FILE.close()
    FILE = open(HOME_DIR + '/.workspaces', 'w')
    FILE.write('1')
else:
    EXEC = 'xdotool set_desktop 0'
    FILE.close()
    FILE = open(HOME_DIR + '/.workspaces', 'w')
    FILE.write('0')

run(EXEC, shell=True)

FILE.close()
