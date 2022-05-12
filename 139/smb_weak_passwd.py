#encoding:utf-8
try:
    import os
    from smb.SMBConnection import SMBConnection
except:
    os._exit(6)

def check(ip,port,user,passwd):
    try:
        conn = SMBConnection(user, passwd, '',"", use_ntlm_v2 = True) 
        assert conn.connect(ip, port)
    except:
        return False
    try:
        return True
    except Exception as e:
        pass

def get_text(ip,port):
    users = []
    passwds = []

    users_file = open ("../dic/dic_username_smb.txt",'r')
    for user in users_file:
        users.append(user.strip())
    users_file.close()

    passwords_file = open("../dic/dic_password_smb.txt",'r')
    for password in passwords_file:
        passwds.append(password.strip())
    passwords_file.close()

    for user_use in users:
        for passswdds in passwds:
            if check(ip,port,user_use,passswdds):
                print("[+] {} find smb weak password".format(ip))
                return 1
    print("[-] {} do not found smb weak passwd".format(ip))
    return 2

def main(ip,port):
    get =  get_text(ip,port)
    os._exit(get)
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))