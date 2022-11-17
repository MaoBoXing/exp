#encoding:utf-8
try:
    import os
    import threading
    import logging
    from multiprocessing.pool import ThreadPool
    logging.basicConfig(level=logging.INFO,format='%(message)s')
    import ftplib
    import Queue
    import datetime
except Exception as e:
    logging.info(e)
    os._exit(6)
Is_True = False
users_passwds =[]
username_list=["amin",'root','111','ems','oracle','sifang','sunri','tx','ut','ut1','administrator','test','admin','web','user']
password_list=['root','@123qwe!@#QWE','user','su-4000361515','sf-4000361515','oracle','nr2000','root123','qwer1234','narins2000','Nems-9700','Abc123','Nroot-9700','123456','ut','UT#2015','UT#20150306','Ab#20150306','q+12345','Admin@322','ytdf_000','ytdf000','111111''ftp','Passw0rd','admin123','admin888','administrator','administrator123','ftppass','password','12345','1234','123','qwerty','test','1q2w3e4r','1qaz2wsx','qazwsx','123qwe','123qaz','0','1234567','123456qwerty','password123','12345678','1q2w3e','okmnji','test123','123456789','q1w2e3r4','mysql','web']

queues = Queue.Queue(len(username_list)*len(password_list))
user_passwd = []
for user in username_list:
    for passwd in password_list:
        queues.put({user:passwd})


def ftp(ip,port,threadId):
    while not queues.empty():
        try:
            user_passwd = queues.get(False)
            strUser=user_passwd.keys()[0]
            strPwd=user_passwd.values()[0]
        except Exception as ex:
            return
        global Is_True,users_passwds
        try:
            ftp = ftplib.FTP()
            ftp.connect(ip,str(port),timeout = 1)
            ftp.login(strUser,strPwd)
            ftp.quit()
            users_passwds.append({strUser:strPwd})
            Is_True = True
        except Exception as e:
            ftp.close()
            pass
    

def main(ip,port):
    threadIP = ThreadPool(16)
    for threadId in range(16):
        threadIP.apply_async(ftp,args=(ip,port,threadId))
    threadIP.close()
    threadIP.join()

    if Is_True==True:
        logging.info("[+] {} find ftp weak passw  user-passwd : {} ".format(ip,users_passwds))
        os._exit(1)
    logging.info("[-] {} do not found ftp weak passwd".format(ip))
    os._exit(2)

if __name__=="__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))
