from pexpect import pxssh
import getpass

def send_command(s,cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before

def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host,user,password)
        return s
    except:
        print '[-] Error Connecting'
        exit(0)

s = pxssh.pxssh()
hostname = raw_input('hostname: ')
username = raw_input('username: ')
password = getpass.getpass('password: ')
s.PROMPT= 'SSH> '
s.login(hostname,username,password,auto_prompt_reset=False)
s.sendline('uptime')
s.prompt()
print s.before


#s = connect('127.0.0.1','guoyingying','123456')
send_command(s,'cat /etc/shadow | grep root')