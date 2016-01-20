import paramiko
import time
import getpass
import sys

####### at the moment this script is only for switchport mode access #######

def sh_interfaces(ip,username,password,output_buffer):

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
    output = remote_conn.recv(output_buffer)

    # See what we have
    print output

    # Now let's try to send the sw a command
    ##### add new config #####
    remote_conn.send("sh int status\n"
    +"\n")

    # Wait for the command to complete
    time.sleep(2)

    output = remote_conn.recv(output_buffer)
    # See what we have
    print output

def new_config_switchport(ip,username,password,name_interface,vlan_id,output_buffer):

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
    output = remote_conn.recv(output_buffer)

    # See what we have
    print output

    # Now let's try to send the router a command
    remote_conn.send("\n"
    +"conf t\n"
    +"interface "+name_interface+"\n"
    +"description DEV-TEAM\n"
    +"switchport mode access\n"
    +"switchport access vlan "+vlan_id+"\n"
    +"spanning-tree bpduguard enable\n"
    +"no shut\n"
    +"end\n"
    +"\nshow run int "+name_interface+"\n"
    +"\nwr\n")

    # Wait for the command to complete
    time.sleep(3)

    output = remote_conn.recv(output_buffer)
    # See what we have
    print output

def checkconfig_switchport(ip,username,password,name_interface,output_buffer):
    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    print "SSH connection established to %s" % ip+"\n"

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session established - to Check config on SW\n"

    # Strip the initial router prompt
    output = remote_conn.recv(output_buffer)

    # See what we have
    print output


    # Now let's try to send the router a command
    remote_conn.send("\n"
    +"show run int "+name_interface+"\n")

    # Wait for the command to complete
    time.sleep(2)

    output = remote_conn.recv(output_buffer)
    # See what we have
    print output

if __name__ == '__main__':

    # VARIABLES
    ip = 'xx.xx.xx.xx'
    output_buffer = 1000000
    name_switch = 'name of device'
    name_interface = 'PORT'
    vlan_id='number'



    option = raw_input("\n"
    +"##################### SWITCHING #####################\n"
    +"\n"
    +"\n"
    +"Please choose one of the otpions below:\n"
    +"\n"
    +"[1] - Configure a new switchport on switch - " + name_switch +"\n\n"
    +"[2] - "+name_switch+"- show interface configuration on " + name_interface +"\n\n"
    +"[3] - Show all ports on " + name_switch +"\n\n"
    +"[option]:")

    print "\n\n##################### TACACS Login #####################\n"
    username = raw_input('\ninsert your username:')
    password = getpass.getpass("Enter your password:")

    if (option == '1'):
        print "###### CONFIG NEW SWITCHPORT ########\n"
        new_config_switchport(ip,username,password,name_interface,vlan_id,output_buffer)
        sys.exit(0)

    if (option == '2'):
        print "\n###### INTERFACE CONFIGURATION ########\n"
        checkconfig_switchport(ip,username,password,name_interface,output_buffer)
        sys.exit(0)

    if (option == '3'):
        print "###### INTERFACES ########\n"
        sh_interfaces(ip,username,password,output_buffer)
        sys.exit(0)

    sys.exit(0)
