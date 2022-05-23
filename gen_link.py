from api import b64e
a=input("Press the Kemono_Link->")
b=b64e(a)
link="KPD://"+b
with open("result.txt","w",encoding="utf-8") as f:
    f.write(link)
print(link+" -> result.txt")


