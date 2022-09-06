from concurrent.futures import ThreadPoolExecutor
import time
import paramiko

def conhost(host):
    user="user"
    pwd="pwd"
    port=22
    sshcon=paramiko.SSHClient()
    sshcon.connect(host,user,pwd,port)
    return sshcon

def upgradefunc(host):
    #cli cmd
    cli="binary path+executable name - msi, exe, rpm, deb"
    api=#post call - binary details
    cmd="software upgrade silent way"
    cmd=["c1","c2","c3"]
    #nfs/smb copy func #just mount a nfs file in the
    conobs=conhost(host)
    #post call if not cmd cli
    results=[]
    for cmd in cmds:
        results.append(conobs.exec_command(cmd))
        #tuple stdin,stdout,stderr
    # untill the package install/upgrade is done
    waitstatus=wait( if install = False, timeout)
    if waitstatus:
        return host,True
    else:
        return host,waitstatus.err

def wait(condition, timeout=600):
    start=time.time()
    end=time.time()+timeout
    while start<end:
        upgradestatus=upgradecheck()
        if upgradestatus:
            return True
        else:
            time.sleep(5)
    return upgradestatus.err

#if direct api based - no need for the ssh/psexec connectors #api token - api login
def psexec(): #windows communication

#get host from some json/inventory files - json/yml
Hosts=[h1,h2,h3]

with ThreadPoolExecutor as Thexec:
    results=Thexec.map(upgradefunc(),Hosts)
    for result in results:
        print(result)
