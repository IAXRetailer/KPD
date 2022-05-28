import os
def sendtorpc(resourcefolder,artist,rpcport):
    import json
    from urllib.request import urlopen
    from . import litelogger
    total=os.listdir(resourcefolder+"/url/"+artist)
    for i in total:
        urllists=open(resourcefolder+"/url/"+artist+"/"+i,"r",encoding="utf-8").read().splitlines()
        b=i.replace(".txt","")
        for url in urllists:
            jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 'qwer',
                                        'method': 'aria2.addUri',#"\""+resourcefolder+"/lib/"+artist+"/"+b+"\""
                                        'params': [[url],{'refer': url,'dir':resourcefolder+"/lib/"+artist+"/"+b}],
                                        }).encode()
            c = urlopen('http://localhost:'+rpcport+'/jsonrpc', jsonreq)
            litelogger.infolog("Send "+url+" to aria")