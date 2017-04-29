#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" This file execute de switch betten workspaces. """
from subprocess import run, check_output
import os

ACTUAL_DESKTOP = int(check_output('xdotool get_desktop', shell=True))
NUM_DESKTOPS = int(check_output('xdotool get_num_desktops', shell=True))

if ACTUAL_DESKTOP == NUM_DESKTOPS - 1:
    ACTUAL_DESKTOP = -1

EXEC = 'xdotool set_desktop {0}'.format(ACTUAL_DESKTOP + 1)
run(EXEC, shell=True)

print(ACTUAL_DESKTOP)
print(NUM_DESKTOPS)

