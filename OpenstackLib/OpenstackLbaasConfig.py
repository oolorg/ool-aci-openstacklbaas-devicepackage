from openstack_base import openstack_base
from lbaas import openstack_lbaas
from neutron import neutron

class OpenstackLbaasConfig:
    opbase_obj = openstack_base

    password = ""
    username = ""
    tenantname = ""
    openstack_ip = ""

    lb_pool_name = ""
    subnet_name = ""
    lb_vip_name = ""
    pool_id = ""

    def init(self):
        print "lb init"

        self.opbase_obj.password = 'password'
        #opbase_obj.password = 'okinawa1940'
        self.opbase_obj.username = 'admin'
        self.opbase_obj.tenantname = 'admin'

        #opbase_obj.openstack_ip = '192.168.1.29'
        self.opbase_obj.openstack_ip = '192.168.99.53'
        self.lb_pool_name = 'test_pool2'
        self.subnet_name = 'test-aci2-nw-sb'
        self.lb_vip_name = 'test_vip'


    def create_lb(self):
        print "create start"
        self.opbase_obj.get_token()
        self.pool_id = openstack_lbaas.create_pools(self.opbase_obj,self.lb_pool_name)
        helthmoniter_id = openstack_lbaas.create_health_monitors(self.opbase_obj)
        openstack_lbaas.associate_health_monitors(self.opbase_obj,self.pool_id,helthmoniter_id)

        subnet_id = neutron.get_subnet_id(self.opbase_obj,self.subnet_name)

        openstack_lbaas.create_vip(self.opbase_obj,self.lb_vip_name,subnet_id,self.pool_id)

    def create_member(self,targetip):
        openstack_lbaas.create_member(self.opbase_obj,self.pool_id,targetip)


