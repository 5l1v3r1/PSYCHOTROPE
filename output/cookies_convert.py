#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from platform import system
import time
from time import time as timer

import sys


def clearscrn():
	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
		os.system('color a')
		os.system('title [+] COD3D By Capitos Kamal | Anonymous Imazighen | Morocco | [+]')
clearscrn()

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)

def print_logo():
	bx = """
	\033[1;91m		


      d8888b. .d8888. db    db  .o88b. db   db  .d88b.  d888888b d8888b.  .d88b.  d8888b. d88888b  \033[1;94m
      88  `8D 88'  YP `8b  d8' d8P  Y8 88   88 .8P  Y8. `~~88~~' 88  `8D .8P  Y8. 88  `8D 88'      \033[1;97m
      88oodD' `8bo.    `8bd8'  8P      88ooo88 88    88    88    88oobY' 88    88 88oodD' 88ooooo  \033[1;99m
      88~~~     `Y8b.    88    8b      88~~~88 88    88    88    88`8b   88    88 88~~~   88~~~~~  \033[1;92m
      88      db   8D    88    Y8b  d8 88   88 `8b  d8'    88    88 `88. `8b  d8' 88      88.      \033[1;95m
      88      `8888Y'    YP     `Y88P' YP   YP  `Y88P'     YP    88   YD  `Y88P'  88      Y88888P  \033[1;90m
                                                                                              
\033[1;93m                                                                                                       
					🔰 Script Name : \033[5;91m|Psychotrope
	                	Yap : \033[1;93mFuck\033[0;92m\033[1;92mAll  \033[5;91m|Imazighen\033[5;92mMorocco| \033[0;96m\033[1;96mThis Tools \033[94mNot are not free\033[90m \033[93m
	"""
	print(bx)
	slowprint("\t\t\t\t\tCOD3D By : Capitos Kamal " + "\n\t\t\t\t\t\t            Contact Me : https://www.instagram.com/capitoskamal/")
print_logo()

if sys.version_info < (3, 0):
    sys.stdout.write("\033[1;96m[-] \033[1;91;40mSorry, This Script requires Python 3.x :(\n\n")
    sys.exit(1)

from http.cookies import SimpleCookie
azbug = input("\n\t\033[1;96m[\033[1;92m+\033[1;96m] \033[1;92mPut Your Cookies :) : ")
cookie = SimpleCookie()
cookie.load(azbug)
cookies = {}
for key, azbug2 in cookie.items():
    cookies[key] = azbug2.value
print("\n\033[1;95;40m* Cookie Converted Success : \033[1;96;40m\n\n" + str(cookies) + "\n\033[0m")
print("   \033[1;93;40m[!] \033[1;91;40mNote: \033[1;94;40mCopy The Converted Cookies, And Past It In Script (azbug.py) in cookies = {''} !\033[0m\n")
