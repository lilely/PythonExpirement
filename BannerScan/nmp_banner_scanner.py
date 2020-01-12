import nmap
import optparse

def callback_result(host, scan_result):
    print '------------'
    print host, scan_result

def nmapScan(tgtHost,tgtPort):
    nmScan = nmap.PortScanner()
    try:
        print('Host:{0}, Port:{1}'.format(tgtHost,tgtPort))
        nmScan.scan(tgtHost,tgtPort)
        scanInfo = nmScan.scaninfo()
        for host in nmScan.all_hosts():
            for key in nmScan[host]['tcp'].keys():
                print('Host:{0},{1},{2}'.format(host,key,nmScan[host]['tcp'][key]))
    except Exception,e:
        print('execption is {0}'.format(e))

def main():
    parser = optparse.OptionParser()
    parser.add_option('-H',dest='tgtHost',type='string',\
            help = 'specify target host')
    parser.add_option('-P',dest='tgtPorts',type='string',\
            help = 'specify target ports')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = options.tgtPorts
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    nmapScan(tgtHost,tgtPorts)
        

if __name__ == '__main__':
    main()

