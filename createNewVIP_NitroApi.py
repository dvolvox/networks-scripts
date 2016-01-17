from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonitor import lbmonitor
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_rewritepolicy_binding import lbvserver_rewritepolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.network.rnat import rnat
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsacls import nsacls
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsconfig import nsconfig
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsmode import nsmode
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nspbrs import nspbrs
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpgroup import snmpgroup
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey import sslcertkey
from nssrc.com.citrix.netscaler.nitro.resource.config.cache.cacheobject import cacheobject
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcipher import sslcipher
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.ssldhparam import ssldhparam
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslpkcs12 import sslpkcs12
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslpkcs8 import sslpkcs8
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslvserver import sslvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslvserver_sslcertkey_binding import sslvserver_sslcertkey_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.system.systemgroup_systemuser_binding import systemgroup_systemuser_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.vpn.vpnvserver_vpnclientlessaccesspolicy_binding import vpnvserver_vpnclientlessaccesspolicy_binding
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service
from nssrc.com.citrix.netscaler.nitro.resource.config.aaa.aaaglobal_aaapreauthenticationpolicy_binding import aaaglobal_aaapreauthenticationpolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.aaa.aaapreauthenticationaction import aaapreauthenticationaction
from nssrc.com.citrix.netscaler.nitro.resource.config.aaa.aaapreauthenticationpolicy import aaapreauthenticationpolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwconfidfield import appfwconfidfield
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwprofile import appfwprofile
from nssrc.com.citrix.netscaler.nitro.resource.config.authentication.authenticationvserver_auditnslogpolicy_binding import authenticationvserver_auditnslogpolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.authentication.authenticationvserver_authenticationlocalpolicy_binding import authenticationvserver_authenticationlocalpolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.server import server
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup import servicegroup
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup_servicegroupmember_binding import servicegroup_servicegroupmember_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.cspolicy import cspolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver_cmppolicy_binding import csvserver_cmppolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.filter.filterpolicy import filterpolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbservice import gslbservice
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbsite import gslbsite
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver import gslbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver_domain_binding import gslbvserver_domain_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver_gslbservice_binding import gslbvserver_gslbservice_binding
from nssrc.com.citrix.netscaler.nitro.resource.base.base_response import base_response
from nssrc.com.citrix.netscaler.nitro.resource.base.base_responses import base_responses
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsfeature import nsfeature
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsmode import nsmode
from nssrc.com.citrix.netscaler.nitro.resource.config.rewrite.rewritepolicy import rewritepolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.rewrite.rewriteaction import rewriteaction
import sys

class set_vip :
    def __init__(self):
        _ip=""
        _username=""
        _password=""

    @staticmethod
    def main(cls):

        config = set_vip()
        #Define IP of Netscaler
        config.ip = "xx.xx.xx.xx"
        #Username and Password
        config.username = "******"
        config.password = "*****"

        try :
            client = nitro_service(config.ip,"http")
            client.set_credential(config.username,config.password)
            client.timeout = 500
            
            ###### Arguments of respective fields ######

            #Name of Server
            SRVS="prdtestlb00"
            #IP of server
            IP="192.168.1.1"
            #Port of service
            port=80
            #Name of Service
            svc_name="svc-"+str(port)
            #Number of Servers
            j=3
            #Name of LB
            lb_vserver_name="lb-testlb"
            #Name of Cs Vserver
            csvserverhttp= "cs-80-testlb"
            csvserverssl= "cs-443-testlb"
            #IP of CS Vserver
            cs_ip="9.1.2.3"
            ###### END Arguments of respective fields ######

            device = raw_input('Select if you want to create a VIP or Delete a VIP - [addvip] or  [rmvip]:')

            if (device == 'addvip' or device == 'ADDVIP'):
                #Create a new VIP
                config.run_newvip(client, SRVS , IP , svc_name , port , lb_vserver_name,csvserverhttp,csvserverssl,cs_ip,j)

            elif (device == 'rmvip' or device == 'RMVIP'):
                #Delete a new VIP
                config.run_rmvip(client, SRVS , IP , svc_name , port , lb_vserver_name,csvserverhttp,csvserverssl,j)

            client.logout()
        except nitro_exception as  e:
            print("Exception::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::message="+str(e.args))
        return

    def add_server(self, client , SRVS , server_ip ,j) :

        try :
            obj=[ server() for _ in range(j)]
            for l in range (1,j):
                obj[l].name = SRVS+str(l)
                obj[l].ipaddress = server_ip+str(l)
                obj[l].state = "DISABLED"
                server.add(client, obj[l])
                print("add_server -"+obj[l].name+" - Done\n")
                l += 1
        except nitro_exception as e :
            print("Exception::add_server::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_server::message="+str(e.args))

        "Exception::add_server::message="+str(e.args))

    def rm_server(self, client , SRVS ,j) :

        try :
            obj=[ server() for _ in range(j)]
            for l in range (1,j):
                obj[l].name = SRVS+str(l)
                server.delete(client, obj[l])
                print("rm_server -"+obj[l].name+" - Done\n")
                l += 1
        except nitro_exception as e :
            print("Exception::add_server::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_server::message="+str(e.args))

    def add_service(self, client , svc_name , port, SRVS,j) :

        try :
            svc = [service() for _ in range(j)]
            for l in range (1,j):
                svc[l].name = svc_name+"-"+SRVS+str(l)
                svc[l].servername = SRVS+str(l)
                svc[l].port = port
                svc[l].servicetype = service.Servicetype.HTTP
                service.add(client, svc[l])
                print("add_service -"+svc[l].servername+" - Done\n")
                l += 1
        except nitro_exception as e :
            print("Exception::add_service::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_service::message="+str(e.args))

    def rm_service(self, client , svc_name , SRVS,j) :

        try :
            svc = [service() for _ in range(j)]
            for l in range (1,j):
                svc[l].name = svc_name+"-"+SRVS+str(l)
                service.delete(client, svc[l])
                print("rm_service -"+svc[l].name+" - Done\n")
                l += 1
        except nitro_exception as e :
            print("Exception::add_service::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_service::message="+str(e.args))

    def add_lbvserver(self, client,lb_vserver_name) :
        try :
            obj = lbvserver()
            obj.name = lb_vserver_name
            obj.servicetype = lbvserver.Servicetype.HTTP
            response = lbvserver.add(client, obj)
            print("add_lbvserver - Done\n")
            if response.severity and response.severity =="WARNING" :
                print("\tWarning : " + response.message)
        except nitro_exception as e :
            print("Exception::add_lbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_lbvserver::message="+str(e.args))

    def rmlbvserver(self, client,lb_vserver_name):
		try :
			response =lbvserver.delete(client,lb_vserver_name)
			if (response.severity and response.severity == ("WARNING")):
				print("Warning : " + response.message)
			print("rmlbvserver - "+lb_vserver_name+"Done\n")
		except nitro_exception as e :
			print("Exception::rmlbvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e :
			print("Exception::rmlbvserver::message="+str(e.args))

    def addlbvserver_bindings(self, client, lb_vserver_name , svc_name,SRVS,j) :
        try :
            obj = [ lbvserver_service_binding() for _ in range(j)]
            for l in range (1,j):
                print ("l="+str(l))
                obj[l].name = lb_vserver_name
                obj[l].servicename = svc_name+"-"+SRVS+str(l)
                lbvserver_service_binding.add(client, obj[l])
                l += 1
                print("addlbvserver_bindings - "+lbvserver_service_binding.add(client, obj[l])+" -Done\n")

        except nitro_exception as e :
            print("Exception::addlbvserver_bindings::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::addlbvserver_bindings::message="+str(e.args))

    def add_csvserver(self, client,csvserverhttp,csvserverssl,cs_ip) :
        try :
            obj = csvserver()
            obj.name = csvserverhttp
            obj.servicetype = csvserver.Servicetype.HTTP
            obj.ipv46 = cs_ip
            obj.port = 80
            csvserver.add(client, obj)
            print("\nadd_csvserver "+obj.name+"- Done\n")

            obj1 = csvserver()
            obj1.name = csvserverssl
            obj1.servicetype = csvserver.Servicetype.SSL
            obj1.ipv46 = cs_ip
            obj1.port = 443
            csvserver.add(client, obj1)
            print("add_csvserver "+obj1.name+"- Done\n")

        except nitro_exception as e :
            print("Exception::add_csvserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_csvserver::message="+str(e.args))

    def rmcsvserver(self, client, csvserverhttp ,csvserverssl) :

            csvserver.delete(client,csvserverhttp)
            print("rmcsvserver = "+ str(csvserverhttp) + " done\n")

            csvserver.delete(client,csvserverssl)
            print("rmcsvserver = "+ str(csvserverssl) +" done\n")


    #GSLB configs for Vserver, Service and Sites
    def add_gslb_vserver(self, client) :
        try :
            gslbvserver1 = gslbvserver()
            gslbvserver1.name = "gvip1"
            gslbvserver1.servicetype = "http"
            gslbvserver.add(client, gslbvserver1)
            print("add_gslb_vserver - Done")
        except nitro_exception as e :
            print("Exception::add_gslb_vserver::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_gslb_vserver::message="+str(e.args))

    def add_gslb_service(self, client) :
        try :
            port=80
            no=100
            gslbservice1 = gslbservice()
            gslbservice1.servicename = "svc0"
            gslbservice1.ip = "10.102.3.239"
            gslbservice1.maxclient = no
            gslbservice1.port = port
            gslbservice1.sitename = "bangalore1"
            gslbservice1.servicetype = "http"
            gslbservice.add(client, gslbservice1)
            print("add_gslb_service - Done")
        except nitro_exception as e :
            print("Exception::add_gslb_service::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::add_gslb_service::message="+str(e.args))

    # GSLB vserver_service binding
    def bind_gslbvserver_gslbservice(self, client) :
        try :
            obj = gslbvserver_gslbservice_binding()
            obj.name = "gvip1"
            obj.servicename = "svc0"
            gslbvserver_gslbservice_binding.add(client, obj)
            print("bind_gslbvserver_gslbservice - Done ")
        except nitro_exception as e :
            print("Exception::bind_gslbvserver_gslbservice::errorcode="+str(e.errorcode)+" , Message ="+ e.message)
        except Exception as e:
            print("Exception::bind_gslbvserver_gslbservice::message="+str(e.args))

    #Function to create VIP
    def run_newvip(self, client , SRVS , server_ip , svc_name , port , lb_vserver_name,csvserverhttp,csvserverssl,cs_ip ,j) :

        self.add_server(client , SRVS , server_ip ,j)
        self.add_service(client , svc_name , port ,SRVS ,j)
        self.add_lbvserver(client ,lb_vserver_name)
        self.addlbvserver_bindings(client,lb_vserver_name,svc_name,SRVS,j)
        self.add_csvserver(client,csvserverhttp,csvserverssl,cs_ip)

    #Function to Remove VIP
    def run_rmvip(self, client , SRVS , server_ip , svc_name , port , lb_vserver_name,csvserverhttp,csvserverssl,j) :

        self.rmcsvserver(client,csvserverhttp,csvserverssl)
        self.rmlbvserver(client,lb_vserver_name)
        self.rm_service( client , svc_name , SRVS,j)
        self.rm_server(client , SRVS,j)

#
# Main thread of execution
#
if __name__ == '__main__':
    try:
            set_vip().main(set_vip())
    except SystemExit:
        print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")
