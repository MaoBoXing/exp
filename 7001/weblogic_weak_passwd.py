try:
    import logging
    logging.basicConfig(level= logging.INFO,format="%(message)s")
    import requests
    import os
except Exception as e:
     logging.info("[*] {}".format(e))
     os._exit(6)
 
def check(ip,port):
    names=['weblogic','system','portaladmin','guest'] 
    passwds=['Oracle@123','system','portaladmin','guest']
    data={}
    is_true =False
    user_passwd =[]
    for name in names: 
        name=name.rstrip()
        for passwd in passwds:  
            passwd=passwd.rstrip()
    
            data = {'j_username':name,'j_password':passwd}
            
            try:        
                url = "http://"+ip +":"+port +"/console/j_security_check"
                response = requests.post(url,data=data,timeout=5)
                result=response.content
                if  result.count('console.portal')!=0:
                    user_passwd.append({name:passwd})
                    is_true = True
            except: 
                pass
    if is_true == True:
        logging.info("[+] {} find weblogic weak passwd user_passwd : {}".format(ip,user_passwd))
        os._exit(1)
    else:
        logging.info("[-] {} do not found weblogic weak passwd ".format(ip))
        os._exit(2)
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)