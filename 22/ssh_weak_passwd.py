#encoding:utf-8
try:
    import os 
    import paramiko
except :
    os._exit(6)
def check(ip,port,user,pwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,user,pwd,timeout=1)
        return True
    except Exception as e:
        pass

def get_usr_pwd(ip,port):
    users = []
    pwds = []
    users_texts = open("../dic/dic_username_ssh.txt","r")
    for text in  users_texts:
        users.append(text.strip())
    users_texts.close()

    pwds_texts = open("../dic/dic_password_ssh.txt","r")
    for pwd in pwds_texts:
        pwds.append(pwd.strip())
    pwds_texts.close()

    for user in users:
        for pwd in pwds:
            if check(ip,port,user,pwd):
                print("[+] {} find ssh weak password".format(ip))
                return 1
    print("[+] {} find ssh weak password".format(ip))
    return 2

def main(ip,port):
    get =  get_usr_pwd(ip,port)
    os._exit(get)

if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))