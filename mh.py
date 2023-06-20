#coding=utf-8
import os, sys, platform

os.system('xdg-open https://www.facebook.com/mh.mahin.7798?mibextid=ZbWKwL')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf fake.cpython-311.so')
except:
    pass
os.system('rm -rf fake.cpython-311.so')
os.system('git pull')
try:os.mkdir('/sdcard/MAHIN')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('fake.cpython-311.so'):
        os.system('curl -L https://raw.githubusercontent.com/MAHIN-71/MAHIN-PRO/main/fake.cpython-311.so?raw=true -o fake.cpython-311.so') 
        import fake
    else:
        import fake
