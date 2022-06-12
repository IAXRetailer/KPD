import api
import os
from colorama import Fore
title='''
################################################################################


              _        _______  _______  _______  _        _______ 
             | \    /\(  ____ \(       )(  ___  )( (    /|(  ___  )
             |  \  / /| (    \/| () () || (   ) ||  \  ( || (   ) |
             |  (_/ / | (__    | || || || |   | ||   \ | || |   | |
             |   _ (  |  __)   | |(_)| || |   | || (\ \) || |   | |
             |  ( \ \ | (      | |   | || |   | || | \   || |   | |
             |  /  \ \| (____/\| )   ( || (___) || )  \  || (___) |
             |_/    \/(_______/|/     \|(_______)|/    )_)(_______)
                                                                   
     ______   _______           _        _        _______  _______  ______  
    (  __  \ (  ___  )|\     /|( (    /|( \      (  ___  )(  ___  )(  __  \ 
    | (  \  )| (   ) || )   ( ||  \  ( || (      | (   ) || (   ) || (  \  )
    | |   ) || |   | || | _ | ||   \ | || |      | |   | || (___) || |   ) |
    | |   | || |   | || |( )| || (\ \) || |      | |   | ||  ___  || |   | |
    | |   ) || |   | || || || || | \   || |      | |   | || (   ) || |   ) |
    | (__/  )| (___) || () () || )  \  || (____/\| (___) || )   ( || (__/  )
    (______/ (_______)(_______)|/    )_)(_______/(_______)|/     \|(______/ 



################################################################################

'''
print(Fore.GREEN+title)
here=os.getcwd()
try:
    try:
        api.testrpc(6800)
    except:
        os.system("Start aria2c --conf-path=./aria2.conf")
        api.litelogger.infolog("Launch aria2 Successfully")
except:
    api.litelogger.warnlog("Launch aria2 failed,it may be launched before")
api.Icookie=open("cookie.txt","r").read()
if api.Icookie == "":
    api.litelogger.warnlog("There is not a cookie in cookie.txt :( , the task may fail")
api.litelogger.infolog(api.Icookie)
if "resource" not in os.listdir():
    api.litelogger.warnlog("There does't have a resource folder")
    api.litelogger.infolog("Make a resource folder...")
    os.mkdir("resource")
    os.chdir("./resource")
    os.mkdir("lib")
    os.mkdir("cache")
    os.chdir(here)
api.litelogger.infolog("KEMONO DOWNLOADER STARTS SUCCESSFULLY!")
api.litelogger.infolog("The sofeware is all free in \"https://github.com/IAXRetailer/KPD\"(Public)")
url=input("Input an artist'url in kemono->")
if "KPD://" in url:
    url=url.replace("KPD://","")
    url=api.b64d(url)
artist=api.kemono("./resource",url)
rpcport=open("rpcport.txt","r",encoding="utf-8").read()
arialist=api.sendtorpc("./resource",artist,rpcport)
#test action