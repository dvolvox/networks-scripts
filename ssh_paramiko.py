import paramiko
import time
import getpass
import sys


def addnewvip(ip,username,password):

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    print "SSH connection established to %s" % ip+"\n"

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session established\n"

    # Strip the initial router prompt
    output = remote_conn.recv(10000000)

    # See what we have
    print output

    # Turn off paging
    #disable_paging(remote_conn)

    # Now let's try to send the router a command
    remote_conn.send("\n"
    +"add server prdtestlb001 192.168.1.1\n"
    +"add service svc-8080-prdtestlb001 prdtestlb001 HTTP 8080\n"
    +"add cs vserver cs-80-testlb HTTP 1.1.1.1 80 -stateupdate ENABLED -caseSensitive OFF\n"
    +"add cs vserver cs-443-testlb SSL 1.1.1.1 443 -stateupdate ENABLED -caseSensitive OFF\n"
    +"add lb vserver lb-80-testlb.default HTTP\n"
    +"bind lb vserver  lb-80-testlb.default svc-8080-prdtestlb001\n"
    +"bind cs vserver cs-80-testlb -lbvserver lb-80-testlb.default\n"
    +"bind cs vserver cs-443-testlb -lbvserver lb-80-testlb.default\n")

    #Remove config
    remote_conn.send("\n"
    +"rm cs vserver cs-80-testlb\n"
    +"rm cs vserver cs-443-testlb\n"
    +"rm lb vserver lb-80-testlb.default\n"
    +"rm server prdtestlb001\n")

    # Wait for the command to complete
    time.sleep(2)

    output = remote_conn.recv(1000000)
    # See what we have
    print output

def checkconfig(ip,username,password):
    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    print "SSH connection established to %s" % ip+"\n"

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session established - to Check config on NS\n"

    # Strip the initial router prompt
    output = remote_conn.recv(10000000)

    # See what we have
    print output

    # Turn off paging
    #disable_paging(remote_conn)

    # Now let's try to send the router a command
    remote_conn.send("\n"
    +"\n"
    +"show run | g testlb\n")

    # Wait for the command to complete
    time.sleep(2)

    output = remote_conn.recv(1000000)
    # See what we have
    print output

if __name__ == '__main__':

    # VARIABLES
    ip = 'xx.xx.xx.xx'
    username = raw_input('\ninsert your username:')
    password = getpass.getpass("Enter your password:")
    #nameSVRS = raw_input('\ninsert name of servers:')
    #serviceSVRS = int(raw_input('\ninsert service running on servers:'))
    #newvip = raw_input('\ninsert name of New Vip:')
    #vipip1 = raw_input('\ninsert First IP of New Vip:')

    addnewvip(ip,username,password)
    checkconfig(ip,username,password)

    sys.exit(0)
