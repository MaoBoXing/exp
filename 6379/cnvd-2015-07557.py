#encoding:utf-8
try:
    import os
    import socket
    import sys
    import logging
except:
    os._exit(6)

logging.basicConfig(level=logging.INFO,format='%(message)s')
def check(ip, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
    except Exception as e:
        logging.info("[*] time out")
        return 4
    try:
        s.send(b"INFO\r\n")
        result = s.recv(1024)
        if b"redis_version" in result:
            logging.info("[+] {} find redis unauthorized".format(ip))
            return 1
        else:
            logging.info("[-] {} do not found reis unauthorize".format(ip))
            return 2
    except Exception as e:
        logging.info("[*] Someting Error!!")
        return 3
def main(ip,port):
    get = check(ip,port, timeout=10)
    os._exit(get)
if __name__ == '__main__':
    ip=sys.argv[1]
    port=sys.argv[2]
    #port = 6379
    main(ip,port)