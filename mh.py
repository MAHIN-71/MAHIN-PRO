#coding=utf-8
import os, sys, platform

os.system('xdg-open https://www.facebook.com/mh.mahin.7798?mibextid=ZbWKwL')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf mahin.cpython-311.so')
except:
    pass
os.system('rm -rf mahin.cpython-311.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Sarfraz.so'):
        os.system('curl -L https://raw.githubusercontent.com/MAHIN-71/MAHIN-PRO/main/mahin.cpython-311.so?raw=true -o mahin.cpython-311.so') 
        import mahin
    else:
        import mahin
