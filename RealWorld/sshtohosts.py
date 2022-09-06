from paramiko import SSHClient

sh=SSHClient()

hostlist=["host1","host3","host3"]
password="pwd"
user="user1"
port=8080
for host in range(hostlist):
    sh.connect(host,port,user,password)

    #connection established
    cmds=["cmd1","cmd2","cmd3"]
    for cmd in range(cmds):
        stdin, stdout, stderr=sh.exec_command(cmd)






