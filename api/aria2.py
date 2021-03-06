import os
from requests import get
def sendtorpc(resourcefolder,artist,rpcport):
    import json
    from urllib.request import urlopen
    from . import litelogger
    total=os.listdir(resourcefolder+"/url/"+artist)
    for i in total:
        urllists=open(resourcefolder+"/url/"+artist+"/"+i,"r",encoding="utf-8").read().splitlines()
        b=i.replace(".txt","")
        for url in urllists:
            dicta={'refer': url,'dir':resourcefolder+"/lib/"+artist+"/"+b}
            jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 'qwer',
                                        'method': 'aria2.addUri',#"\""+resourcefolder+"/lib/"+artist+"/"+b+"\""
                                        'params': [[url],dicta],
                                        }).encode()
            c = urlopen('http://localhost:'+rpcport+'/jsonrpc', jsonreq)
            litelogger.infolog("Send "+url+" to aria")

def aria_rpctest(port):
    port=str(port)
    return get(f"http://127.0.0.1:{port}/jsonrpc?jsoncallback=test").status_code