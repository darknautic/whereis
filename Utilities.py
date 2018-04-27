#!/usr/bin/python
import os
import getpass
import json
import operator
import time
import threading
import socket


class Utilities:
    clrs = {
        "blue": "\033[94m",
        "green": "\033[92m",
        "gold": "\033[33m",
        "magenta": "\033[95m",
        "turquois": "\033[96m",
        "cyan": "\033[36m",
        "gray": "\033[90m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "redOrg": "\033[91m",
        "endc": "\033[0m",
        "bold": "\033[1m",
        "blink": "\033[5m",
        "reverse": "\033[7m",
        "underline": "\033[4m",
        "header": "\033[104m\033[93m",
        "blk":"\033[0m",
        "err":"\033[91m\033[5m"


    }

def printErr(str):
    print(Utilities.clrs['err']+time.strftime('%d/%h/%Y %H:%M:%S').ljust(22)+'[ERROR] -'.ljust(10)+str+Utilities.clrs['blk'])

def printWrn(str):
    print(Utilities.clrs['yellow']+time.strftime('%d/%h/%Y %H:%M:%S').ljust(22)+'[WARN] -'.ljust(10)+ str+Utilities.clrs['blk'])

def printInf(str):
    print(Utilities.clrs['blue']+time.strftime('%d/%h/%Y %H:%M:%S').ljust(22)+'[INFO] -'.ljust(10)+str+Utilities.clrs['blk'])