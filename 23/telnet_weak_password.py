#encoding:utf-8
try:
    import os
    import telnetlib
except:
    os._exit(6)
def check(ip,port,user,pwd):
    try:
        tn = telnetlib.Telnet(ip,timeout=1)
    except :
        return False
    try:
        tn.set_debuglevel(0)
        tn.read_until("login: ")
        tn.write(user + '\r\n')
        tn.read_until("assword: ")
        tn.write(pwd + '\r\n')
        result = tn.read_some()
        result = result+tn.read_some()
        tn.close()
        if b'Last login'in result:
            print("{} {}".format(user,pwd))
            return True
        else:
            return False 
        
    except Exception as e:
        print(e)
        

def get_user_passwd(ip,port):
    users =[]
    passwords = []
    users_text = open('../dic/dic_username_telnet.txt','r')
    for user in users_text:
         users.append(user.strip())
    users_text.close()
    pass_text = open("../dic/dic_password_telnet.txt","r")
    for password in pass_text:
        passwords.append(password.strip())
    pass_text.close()
    for usr in users:
        for passw in users:
            if check(ip,port,usr,passw):
                print("[+] {} find telnet weak password".format(ip))
                return 1
    print("[-] {} do not ound telnet weak password".format(ip))
    return 2

def main(ip,port):
    get =  get_user_passwd(ip,port)
    os._exit(get)
       

if __name__=="__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))