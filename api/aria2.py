import os
def aria2mklist(resourcefolder,artist):
    commandlist=[]
    total=os.listdir(resourcefolder+"/url/"+artist)
    for i in total:
        b=i.replace(".txt","")
        #aria2c --conf-path="...aria2c.conf" --input-file=test-aria2.txt --dir=DIR
        commandlist.append("aria2c --input-file=\""+resourcefolder+"/url/"+artist+"/"+i+"\" --dir=\""+resourcefolder+"/lib/"+artist+"/"+b+"\"")
    return commandlist