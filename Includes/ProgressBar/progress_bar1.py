#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script:	progress_bar1.py
Date:	2018-09-24

Platform: MacOS

Description:
Creates a text based progress bar

"""
__author__      = "thedzy"
__copyright__   = "Copyright 2018, thedzy"
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "thedzy"
__email__       = "thedzy@hotmail.com"
__status__      = "Developer"

import time
import os, sys

rows, columns = os.popen('stty size', 'r').read().split()
toolbar_width = int(columns) - 5

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("▉")
    sys.stdout.flush()

sys.stdout.write("\n")