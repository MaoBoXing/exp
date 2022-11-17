try:
    import logging,os,requests
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)


def check(ip,port):
    try:
        target = "http://" + ip + ":" + port+ "/api/whoami"
        RabbitMQheaders = {
        'authorization': 'Basic Z3Vlc3Q6Z3Vlc3Q=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        }
        req = requests.get(target,headers=RabbitMQheaders,timeout=3)
        if req.status_code == 200 and "guest" in req.text:
            logging.info("[+] {} find rabbitmq unauthorized".format(ip))
            os._exit(1)
        else:
            logging.info("[-] {} do not found req".format(ip))
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)


if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)