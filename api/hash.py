import base64
def encode(string):
    buf=string.encode("utf-8")
    byt=base64.b64encode(buf)
    result=byt.decode("utf-8")
    return result

def decode(string):
    buf=string.encode("utf-8")
    byt=base64.b64decode(buf)
    result=byt.decode("utf-8")
    return result

