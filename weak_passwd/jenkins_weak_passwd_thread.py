#encoding:utf-8
try:
    import os
    import logging
    logging.basicConfig(level=logging.INFO,format='%(message)s')
    import sys
    import queue
    import requests
    import threading
except:
    os._exit(6)

Is_True = False
username_list=['admin', "pocosin",'111', 'ems', 'oracle', 'sifang', 'sunri', 'tx', 'ut', 'ut1', 'd5000', 'pi3000', 'pi6000', 'oms', 'dky', 'sysadmin', 'netadmin', 'secadmin', 'audadmin', 'mysql', 'dmdbms', 'dmdba', 'kingbase', 'rock', 'rocky', 'h3c', 'h3capadmin', 'superadmin', 'huawei', 'admin', 'administrator', 'anonymous', 'backup', 'ftp', 'guest', 'linux', 'postgres', 'sys', 'system', 'temp', 'test', 'test1', 'tomcat', 'upload', 'user', 'user1', 'web', 'www']
password_list=['admin', 'test', 'root', 'toor', 'su-4000361515', 'sf-4000361515', 'oracle', 'nr2000', 'root123', 'qwer1234', 'narins2000', 'Nems-9700', 'Abc123', 'Nroot-9700', '123456', 'ut', 'UT#2015', 'UT#20150306', 'Ab#20150306', 'q+12345', 'Admin@322', 'ytdf_000', 'ytdf000', '111111', 'sysadmin', 'secadmin', 'audadmin', 'netadmin', 'd5000', 'sysadm', 'netadm', 'secadm', 'audadm', 'dmdbms', 'dmdba', 'kingbase', 'R0ck9', 'pi3000', 'pi6000', 'open3000', 'oms', 'dky', 'rock', 'rocky', 'h3c', 'h3capadmin', 'superadmin', 'huawei', 'DEL.123.com', 'Passw0rd', 'qweasdzxc', 'admin123!@#', 'admin', 'admin123', 'admin@123', 'admin#123', 'password', '12345', '1234', '123', 'qwerty', 'test', '1q2w3e4r', '1qaz2wsx', 'qazwsx', '123qwe', '123qaz', '0000', '1234567', '123456qwerty', 'password123', '12345678', '1q2w3e', 'okmnji', 'test123', '123456789', 'postgres', 'q1w2e3r4', 'redhat', 'user', 'mysql', 'apache']
queues = queue.Queue(len(username_list)*len(password_list))
for user in username_list:
    for passwd in password_list:
        queues.put({user:passwd})

def check(ip,port):
    global Is_True
    user_passwd = queues.get()
    url = "http://"+ip+":"+str(port) + "/j_acegi_security_check"
    data = {
            "j_username" : user_passwd.keys()[0],
            "j_password" : user_passwd.values()[0],
            "from" : "/asynchPeople/",
            "Submit" : "Sign in"
            }
    try:
        response = requests.post(url , data=data,timeout=2)
        if response.status_code == 200:
            
            Is_True = True
            queues.queue.clear() 
    except Exception as e:
        pass


def main(ip,port):
    while 1:
        if threading.active_count()<=50:
            try:
                ssh_threads = threading.Thread(target=check,args=(ip,port))
                ssh_threads.setDaemon(True)
                ssh_threads.start()
                if (queues.empty()==True) or (Is_True==True):
                    break
            except:
                pass
    if Is_True == True:
        logging.info("[+] {} find jenkins weak password".format(ip))
        os._exit(1)
    logging.info("[-] {} do not found jenkins weak password".format(ip))
    os._exit(2)
if __name__ == "__main__":
    # while queues.empty()!= True:
    #     logging.info(queues.get())
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))