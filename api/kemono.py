import requests
import os
from bs4 import BeautifulSoup
from . import litelogger
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
'''
proxies={
'http':'127.0.0.1:8080',
'https':'127.0.0.1:8080'
}
'''
def getpage(url):
    res=requests.get(url,headers=headers)
    res.encoding="utf-8"
    return res.text

def BSpage(text):
    tr=BeautifulSoup(text,"lxml")
    return tr

#https://kemono.party/patreon/user/12281898
def mkcache(cachefolder,filename,msg):
    target=cachefolder+"/"+filename
    f=open(target,"w",encoding="utf-8")
    f.write(msg)
    f.close()
def rdcache(cachefolder,filename):
    target=cachefolder+"/"+filename
    f=open(target,"r",encoding="utf-8").read().splitlines()
    return f

def getartist(calist):
    for i in calist:
        if "</title>" in i and "<title>" in i:
            i=i.replace("<title>Posts of ","").replace(" | Kemono</title>","").replace("from","-")
            break
    litelogger.infolog("Artist "+i)
    return i
def getelements(text):
    tr=BeautifulSoup(text,"lxml")
    rtr=tr.find_all("h2")
    elements=[]
    for i in rtr:
        i=str(i)
        i=i.split("</h2")[0].split(">")[1]
        elements.append(i)
    return elements

def keymapping(keyname,vaule):
    litelogger.infolog("Load "+keyname)
    if keyname == "Comments":
        litelogger.infolog("Comments Pass")
    if keyname == "Downloads":
        rawlist=vaule.split("</a>")
        resulturls=[]
        for i in rawlist:
            if "href" in i:
                aurl=i.split("href=\"")[1].split("\"")[0]
                aurl="https://kemono.party"+aurl
                resulturls.append(aurl)
                litelogger.infolog("Get "+aurl)
        return resulturls
    if keyname == "Content":
        result=vaule.split("class=\"post__content\">")[1].split("</div")[0]
        return result
    if keyname == "Files":
        rawlist=vaule.split("</a>")
        resulturls=[]
        for i in rawlist:
            if "data-src=\"" in i:
                aurl=i.split("data-src=\"")[1].split("\"")[0].replace("/thumbnail","")
                aurl="https://kemono.party"+aurl
                resulturls.append(aurl)
                litelogger.infolog("Get "+aurl)
        return resulturls


def makedir(folder,foldername):
    here=os.getcwd()
    os.chdir(folder)
    if foldername in os.listdir():
        litelogger.warnlog("The folder \""+foldername+"\" has existed")
        os.chdir(here)
        return False
    else:
        os.mkdir(foldername)
        litelogger.infolog("Make folder \""+foldername+"\"")
        os.chdir(here)
        return True
def getmaxobject(obj):
    for i in obj:
        if "Showing" in i:
            break
    try:
        maxnum=int(i.split(" of ")[1])
    except:
        litelogger.errorlog("GET MAX OBJECT WARN")
    return maxnum

def kemonoS(resourcefolder,url):
    ttlist=[]
    tulist=[]
    litelogger.infolog("The URL is \""+url+"\"")
    try:
        tr=BSpage(getpage(url))
        mkcache(resourcefolder+"/cache", "cache.txt", str(tr))
        litelogger.infolog("Make \"cache.txt\"")
    except:
        litelogger.errorlog("Can't connect to \""+url+"\"")
        os.system("pause")
    calist=rdcache(resourcefolder+"/cache", "cache.txt")
    artist=getartist(calist)
    makedir(resourcefolder+"/lib", artist)
    trlist=tr.find_all("h2")
    for i in range(len(trlist)):
        mkcache(resourcefolder+"/cache", "cacheresource.txt", str(trlist[i]))
        #litelogger.infolog("Make&Refresh \"cacheresource.txt\"")
        cdlist=rdcache(resourcefolder+"/cache", "cacheresource.txt")
        title=cdlist[2].replace("          ", "")
        ttlist.append(title)
        reurl=cdlist[1].replace("<a href=\"", "https://kemono.party/").replace("\">", "")
        tulist.append(reurl)
        litelogger.infolog(f"Extract  {title} | {reurl}")
    return ttlist,tulist,artist

def kemonoC(resourcefolder,url):
    ttlist=[]
    tulist=[]
    litelogger.infolog("The URL is \""+url+"\"")
    try:
        tr=BSpage(getpage(url))
        mkcache(resourcefolder+"/cache", "cache.txt", str(tr))
        litelogger.infolog("Refresh \"cache.txt\"")
    except:
        litelogger.errorlog("Can't connect to \""+url+"\"")
        os.system("pause")
    trlist=tr.find_all("h2")
    for i in range(len(trlist)):
        mkcache(resourcefolder+"/cache", "cacheresource.txt", str(trlist[i]))
        #litelogger.infolog("Make&Refresh \"cacheresource.txt\"")
        cdlist=rdcache(resourcefolder+"/cache", "cacheresource.txt")
        title=cdlist[2].replace("          ", "")
        ttlist.append(title)
        reurl=cdlist[1].replace("<a href=\"", "https://kemono.party/").replace("\">", "")
        tulist.append(reurl)
        litelogger.infolog(f"Extract  {title} | {reurl}")
    return ttlist,tulist
def addtutocache(resourcefolder,artist,ttlist,tulist):
    ef=os.listdir(resourcefolder+"/lib/"+artist)
    if "title.txt" not in ef:
        f=open(resourcefolder+"/lib/"+artist+"/title.txt","w")
        f.close()
        litelogger.infolog("Make title.txt")
    f=open(resourcefolder+"/lib/"+artist+"/title.txt","a",encoding="utf-8")
    for i in ttlist:
        i=i+"\n"
        f.write(i)
    f.close()
    litelogger.infolog("Write title into title.txt")
        
    ef=os.listdir(resourcefolder+"/lib/"+artist)
    
    if "urlcache.txt" not in ef:
        f=open(resourcefolder+"/lib/"+artist+"/urlcache.txt","w")
        f.close()
        litelogger.infolog("Make urlcache.txt")
    f=open(resourcefolder+"/lib/"+artist+"/urlcache.txt","a",encoding="utf-8")
    
    
    for i in tulist:
        i=i+"\n"
        f.write(i)
    f.close()
    litelogger.infolog("Write title into urlcache.txt")

def parsesonpage(url,title,artist,resourcefolder):
    
    return

def kemono(resourcefolder,url):
    if "?o=0" in url:
        url.replace("?o=0","")
    url=url+"?o=0"
    order=0
    tt,urllist,artist=kemonoS(resourcefolder,url)
    addtutocache(resourcefolder,artist,tt,urllist)
    maxnum=getmaxobject(rdcache(resourcefolder+"/cache", "cache.txt"))-1
    while order+25 < maxnum:
        oldo="o="+str(order)
        order+=25
        newo="o="+str(order)
        url=url.replace(oldo, newo)
        tt,urllist=kemonoC(resourcefolder,url)
        addtutocache(resourcefolder,artist,tt,urllist)
    urllist=rdcache(resourcefolder+"/lib/"+artist, "urlcache.txt")
    titlelist=rdcache(resourcefolder+"/lib/"+artist, "title.txt")
    unfolderCha="\/:*?\">|<"
    localfolders=[]
    for i in titlelist:
        for j in list(unfolderCha):
            i=i.replace(j, "")
        localfolders.append(i)
        odi=0
        rslt=makedir(resourcefolder+"/lib/"+artist, i)
        while not rslt:
            odi+=1
            i=i+" "+str(odi)
            rslt=makedir(resourcefolder+"/lib/"+artist, i)
        localfolders.append(i)
        os.remove(resourcefolder+"/lib/"+artist+"/title.txt")
        litelogger.infolog("Remove title.txt")
        os.remove(resourcefolder+"/lib/"+artist+"/urlcache.txt")
        litelogger.infolog("Remove urlcache.txt")
    