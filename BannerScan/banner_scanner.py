import optparse
import nmp
from socket import *
from threading import *

screenLock = Semaphore(value = 1)

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('Hello world\r\n')
        resuts = connSkt.recv(100)
        screenLock.acquire()
        print('[+]{}/tcp open '.format(tgtPort))
        print '[+] ' + str(resuts)
    except Exception ,e:
        screenLock.acquire()
        print('[-]{}/tcp closed'.format(tgtPort))
        print('reason is {}'.format(e))
    finally:
        screenLock.release()
        connSkt.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIp = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknow host"%tgtHost
        retrun
    try:
        tgtName = gethostbyaddr(tgtIp)
        print '\n[+] Scan result for :' + tgtName[0]
    except:
        print '\n[+] Scan result for :' + tgtIp
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target = connScan,args=(tgtHost,int(tgtPort)))
        t.start()

def main():
    # parser = optparse.OptionParser('usage%prog '+'\
    #     '-H <target_host> -p <target_port>')
    parser = optparse.OptionParser()
    parser.add_option('-H',dest='tgtHost',type='string',\
            help = 'specify target host')
    parser.add_option('-P',dest='tgtPorts',type='string',\
            help = 'specify target ports')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = options.tgtPorts.split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print parser.usage
        exit(0)
    portScan(tgtHost,tgtPorts)
    
if __name__ == "__main__":
    main()