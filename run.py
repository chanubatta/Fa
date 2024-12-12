#coding=utf-8
import os, sys, platform
os.system('rm -rf myT')
os.system('git pull')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf myT')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('myT'):
        os.system('curl -L https://github.com/Niki404-Cyber/nikifiles/blob/main/myT?raw=true -o myT')
        os.system('chmod 777 myT;./myT')
    else:
        os.system('chmod 777 myT;./myT')
