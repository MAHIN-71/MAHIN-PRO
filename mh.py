import platform
import os
try:os.system("xdg-open https://youtube.com/@mhmahin8427")
try:os.system("xdg-open https://chat.whatsapp.com/Iwto8kUxcbFK4EuifbillQ")
except:pass
try:os.system("clear")
except:pass
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('touch .prox.txt')
except:pass
try:os.system('touch .proxy.txt')
except:pass
try:os.mkdir('/sdcard/OK')
except:pass
try:os.mkdir('/sdcard/CP')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
        __import__("latter")._site_view_()
elif 'aarch' in arc:
        __import__("mh").menu()
else:
        exit(f' Unknow device machine {arc}')
