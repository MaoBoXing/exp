#encoding:utf-8
try:
    import os
    import threading
    import logging
    logging.basicConfig(level=logging.INFO,format='%(message)s')
    import ftplib
    import Queue
except Exception as e:
    logging.info(e)
    os._exit(6)
Is_True = False
username_list=['ftp','user',"amin",'root','111','ems','oracle','sifang','sunri','tx','ut','ut1','user','administrator','test','admin','web']
password_list=['ftp','root','@123qwe!@#QWE','user','su-4000361515','sf-4000361515','oracle','nr2000','root123','qwer1234','narins2000','Nems-9700','Abc123','Nroot-9700','123456','ut','UT#2015','UT#20150306','Ab#20150306','q+12345','Admin@322','ytdf_000','ytdf000','111111','user','ftp','Passw0rd','admin123','admin888','administrator','administrator123','ftppass','password','12345','1234','123','qwerty','test','1q2w3e4r','1qaz2wsx','qazwsx','123qwe','123qaz','0','1234567','123456qwerty','password123','12345678','1q2w3e','okmnji','test123','123456789','q1w2e3r4','mysql','web']
queues = Queue.Queue(len(username_list)*len(password_list))
user_passwd = []
for user in username_list:
    for passwd in password_list:
        queues.put({user:passwd})


def ftp(ip,port):
        global Is_True,user_passwd
        user_passwd = queues.get()
        try:
            # logging.info("=")
            ftp = ftplib.FTP()
            ftp.connect(ip,str(port),timeout = 1)
            ftp.login(user_passwd.keys()[0],user_passwd.values()[0])
            ftp.quit()
            Is_True = True
            user_passwd.append({user_passwd.keys()[0]:user_passwd.values()[0]})
            queues.queue.clear()
        except Exception as e:
            ftp.close()
            pass 
    

def main(ip,port):
    thread = []
    while 1:
        if threading.active_count() <= 50:
            try:
                ftp_thread = threading.Thread(target=ftp,args=(ip,port))
                ftp_thread.setDaemon(True)
                ftp_thread.start()
                thread.append(ftp_thread)
                if (queues.empty()==True) or(Is_True==True):
                    break
            except:
                pass
    for i in range(len(thread)):
        thread[i].join(3)
    if Is_True==True:
        # logging.info(user_passwd)
        logging.info("[+] {} find ftp weak passw  user: {} , passwd: {}".format(ip,user_passwd.keys()[0],user_passwd.keys()[0]))
        os._exit(1)
    logging.info("[-] {} do not found ftp weak passwd".format(ip))
    os._exit(2)
if __name__=="__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))
    # while queues.empty()!=True:
    #     logging.info(queues.get().values()[0])