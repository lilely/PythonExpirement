from pexpect import pxssh

class Client:
    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            print '[+] host:' + self.host + 'user:' + self.user + 'pssword' + self.password
            s.login(self.host,self.user,self.password,auto_prompt_reset=False)
            print '[+] Password Found: ' + self.password
            return s
        except Exception,e:
            print e 
            print '[-] Error Connecting'
        
    def sendCommand(self,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def botnetCommand(command):
    for Client in botNet:
        upput = Client.sendCommand(command)
        print '[+] Output from ' + Client.host + upput
    
    
def addClient(host,user,password):
    client = Client(host,user,password)
    botNet.append(client)

botNet = []
addClient('127.0.0.1','jinlong','123456')
addClient('127.0.0.1','guoyingying','123456')
botnetCommand('ls -l')
botnetCommand('ps')
