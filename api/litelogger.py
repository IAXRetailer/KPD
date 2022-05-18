import colorama
import datetime

colorama.init(autoreset=True)
def gettime():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

#print log
def infolog(msg):
    print(colorama.Fore.GREEN+f"[INFO | {gettime()}] "+colorama.Fore.WHITE+msg)

def warnlog(msg):
    print(colorama.Fore.YELLOW+f"[WARN | {gettime()}] "+colorama.Fore.YELLOW+msg)
    
def errorlog(msg):
    print(colorama.Fore.RED+f"[ERROR | {gettime()}] "+colorama.Fore.RED+msg)
    
