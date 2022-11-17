#encoding:utf-8
try:
    import requests,os,sys,logging,socket,threading
    requests.packages.urllib3.disable_warnings()
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)


def get_my_ip(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(3)
    s.connect((ip,int(port)))
    my_ip = s.getsockname()
    s.close()
    return(my_ip[0])


def listen(ip,listen_port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
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





def check(ip,port):
    target = "http://" + ip + ":" + port
    payload = "                 "                                                                           #填写payload
    header = {
        
    }                                                                                                       #填写header头
    data = "        "                                                                                       #填写data数据
    try:
        req = requests.post(url=target+payload,headers=header,data=data,timeout=3,verify=False,allow_redirects=False)

        if req.status_code == 200:
            if (b'    ' in req.text) and  (b'    ' in req.text) and (b'     ' in req.text):                 #填写判断条件
                logging.info("[+] {} find            ".format(ip))                                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found            ".format(ip))                                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)






def main(ip,port):
    listen_port =                                                                                            #填写监听端口
    my_ip = get_my_ip(ip,port)
    listening = threading.Thread(target=listen,args=(ip,))
    listening.start()

    check(ip,port,my_ip,listen_port)


if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,port)