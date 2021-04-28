# -*- coding: utf-8 -*-
"""
Created by Leon at 4/28/2021

"""
__author__ = "Leon"
__version__ = "0.0.1"
__email__ = "yang.li@zillnk.com"

import ctypes
from ctypes import *
# print(windll.kernel32)
# print(cdll.msvcrt)
# print(hex(windll.kernel32.GetModuleHandleA(None)))
cdll.msvcrt.printf(b"%s %d %f\n", b"X", 2, 3)