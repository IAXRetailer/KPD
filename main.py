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
customargvs=open("customargvs.txt","r",encoding="utf-8").read()
arialist=api.aria2mklist("./resource",artist,customargvs)
for i in arialist:
    os.system(i)
#test action