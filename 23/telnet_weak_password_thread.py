#encoding:utf-8

try:
    import os
    import telnetlib
    import logging
    logging.basicConfig(level=logging.INFO,format='%(message)s')
    import queue
    from multiprocessing.pool import ThreadPool
except Exception as e:
    print(e)
    os._exit(6)
Is_True = False
users_passws = []
username_list=['pocosin','root', 'user', 'admin', 'H3C', '111', 'ems', 'oracle', 'sifang', 'sunri', 'tx', 'ut', 'ut1', 'huawei', 'h3c', 'h3capadmin', 'superadmin', 'rock', 'rocky', 'sysadmin', 'secadmin', 'audadmin', 'guest', 'ftp', 'www']
password_list=['toor', 'user', '123456', 'root', 'su-4000361515', 'sf-4000361515', 'oracle', 'nr2000', 'root123', 'qwer1234', 'narins2000', 'Nems-9700', 'Abc123', 'Nroot-9700', 'ut', 'UT#2015', 'UT#20150306', 'Ab#20150306', 'q+12345', 'Admin@322', 'ytdf_000', 'ytdf000', '111111', 'admin', 'huawei', 'H3C', 'DEL.123.com', 'admin_default', 'sysadmin', 'secadmin', 'audadmin', 'netadmin', 'd5000', 'sysadm', 'netadm', 'secadm', 'audadm', 'dmdbms', 'dmdba', 'kingbase', 'R0ck9', 'pi3000', 'pi6000', 'open3000', 'oms', 'dky', 'rock', 'rocky', 'h3c', 'h3capadmin', 'superadmin', 'qweasdzxc', 'Passw0rd', 'password', '12345', '1234', '123', 'qwerty', 'test', '1q2w3e4r', '1qaz2wsx', 'qazwsx', '123qwe', '123qaz', '0', '1234567', '123456qwerty', 'password123', '12345678', '1q2w3e', 'okmnji', 'test123', '123456789', 'q1w2e3r4', 'apache']
queues = queue.Queue(len(username_list)*len(password_list))
for user in username_list:
    for passwd in password_list:
        queues.put({user:passwd})


def check(ip,port):
    while not queues.empty():
        try:
            global Is_True,users_passws
            user_passwd = queues.get(False)
            tn = telnetlib.Telnet(ip,port=port,timeout=3)
        except :
            return
        try:
            tn.set_debuglevel(0)
            tn.read_until("login: ")
            tn.write(user_passwd.keys()[0] + '\r\n')
            tn.read_until("assword: ")
            tn.write(user_passwd.values()[0] + '\r\n')
            result = tn.read_some()
            result = result+tn.read_some()
            tn.close()
            if (b'Welcome'in result) or (b'Last login:' in result):
                users_passws.append({user_passwd.keys()[0]:user_passwd.values()[0]})
                Is_True=True        
        except Exception as e:
            logging.info(e)
            users_passws.append(user_passwd)
            # if 
            pass
def main(ip,port):
    threadIP = ThreadPool(50)
    for threadId in range(50):
        threadIP.apply_async(check,args=(ip,port))
    threadIP.close()
    threadIP.join()

    if Is_True == True:
        logging.info("[+] {} find telnet weak passwd user_passwd : {}".format(ip,users_passws))
        os._exit(1)
    logging.info("[-] {} do not found telnet weak passwd".format(ip))
    os._exit(2)
if __name__=="__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))