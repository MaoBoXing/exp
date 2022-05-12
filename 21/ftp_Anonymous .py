#encoding:utf-8
try:
    import os 
    import ftplib
    import logging
except Exception as e :
    os._exit(6)

logging.basicConfig(level=logging.DEBUG,format='%(message)s')
def check(ip,port):
    
    try:
        ftp = ftplib.FTP()
        ftp.connect(ip,port,timeout=1)
    except:
        logging.info("[*] time out")
        return 4
    try:
        ftp.login('anonymous','anonymous')
        logging.info("[+] {} find FTP Anonymous".format(ip))
        return 1
    except Exception as e:
        logging.info("[-] {} do not found Anonymous".format(ip))
        return 2
def main(ip,port):
    get =  check(ip,port)    
    os._exit(get)

if __name__ == '__main__':
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,port)

    