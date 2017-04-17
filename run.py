#!/usr/bin/python3
# -*- coding: utf-8 -*-
from subprocess import check_output, run

file = open('file', 'r')

command = 'xdotool get_desktop'
# active_workspace = 0

# if int(check_output(command, shell=True)) == 0:
#     print('1111111111111111111')
# else:
#     print('DIOASNIODNAS')

if int(file.read()) == 0:
    command = 'xdotool set_desktop 1'
    file.close()
    file = open('file', 'w')
    file.write('1')
else:
    command = 'xdotool set_desktop 0'
    file.close()
    file = open('file', 'w')
    file.write('0')

run(command, shell=True)

file.close()
