import httplib2
#from openstack_base import openstack_base
import json
import sys

class openstack_lbaas:
    @classmethod
    def create_pools(self,ops_base_obj,name):

        print "create pool"

#        url = "http://192.168.151.185:9696/v2.0/lb/pools"

        url = 'http://'+ ops_base_obj.openstack_ip +':9696/v2.0/lb/pools'

#        body = '{' \
#       '"pool":{' \
#        '"subnet_id": "'+ops_base_obj.subnet_id+'",' \
#        '"lb_method": "'+'ROUND_ROBIN'+'",' \
#        '"protocol": "'+'HTTP'+'",' \
#        '"name": "'+name+'",' \
#        '"admin_state_up": "True"' \
#        '}' \
#       '}'
        body = '{' \
       '"pool":{' \
        '"subnet_id": "ada8a739-60c3-4205-8482-b24eb5c950ce",' \
        '"lb_method": "'+'ROUND_ROBIN'+'",' \
        '"protocol": "'+'HTTP'+'",' \
        '"name": "' + name + '",' \
        '"admin_state_up": "True"' \
        '}' \
       '}'
        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid,'Content-Type':'application/json'}
        resp, rest_res = h.request(url, 'POST', headers=headers, body=str(body))
        if "202" == resp.get("status") or "201" == resp.get("status"):
            rest_result = rest_res.decode(sys.stdin.encoding)
            pool_result = json.loads(rest_result)
            pool_id = str(pool_result['pool']['id'])
            print "create success id:"+str(pool_result['pool']['id'])
        else:
            pool_id='fail'
            print "create fail"
            print str(resp)
            print str(rest_res)

        return pool_id

    @classmethod
    def create_health_monitors(self,ops_base_obj):

        print "create health monitors"

#        url = "http://192.168.151.185:9696/v2.0/lb/health_monitors"

        url = 'http://'+ ops_base_obj.openstack_ip +':9696/v2.0/lb/health_monitors'

        body = '{' \
       '"health_monitor":{' \
        '"delay": "5",' \
        '"max_retries": "3",' \
        '"type": "HTTP",' \
        '"timeout": "2",' \
        '"admin_state_up": "True"' \
        '}' \
       '}'
#        body = '{' \
#       '"pool":{' \
#        '"subnet_id": "ada8a739-60c3-4205-8482-b24eb5c950ce",' \
#        '"lb_method": "'+'ROUND_ROBIN'+'",' \
#        '"protocol": "'+'HTTP'+'",' \
#        '"name": "'+name+'",' \
#        '"admin_state_up": "True"' \
#        '}' \
#       '}'
        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid,'Content-Type':'application/json'}
        resp, rest_res = h.request(url, 'POST', headers=headers, body=str(body))
        if "202" == resp.get("status") or "201" == resp.get("status"):
            rest_result = rest_res.decode(sys.stdin.encoding)
            health_monitor_result = json.loads(rest_result)
            health_monitor_id = str(health_monitor_result['health_monitor']['id'])
            print "create success id:"+str(health_monitor_result['health_monitor']['id'])
        else:
            health_monitor_id = 'fail'
            print "create fail"
            print str(resp)
            print str(rest_res)

        return health_monitor_id

    @classmethod
    def associate_health_monitors(self,ops_base_obj,pool_id,helth_monitor_id):
        print "associate health monitors"

#        url = "http://192.168.151.185:9696/v2.0/lb/health_monitors"

        url = 'http://'+ ops_base_obj.openstack_ip +':9696/v2.0/lb/pools/' + pool_id +'/health_monitors'

        body = '{' \
       '"health_monitor":{' \
        '"id": "' + helth_monitor_id + '"' \
        '}' \
       '}'

        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid,'Content-Type':'application/json'}
        resp, rest_res = h.request(url, 'POST', headers=headers, body=str(body))
        print str(resp)
        print str(rest_res)
        return


    @classmethod
    def create_vip(self,ops_base_obj,vip_name,subnet_id,pool_id):

        print "create vip"

#        url = "http://192.168.99.225:9696/v2.0/lb/vips"

        url = 'http://'+ ops_base_obj.openstack_ip +':9696/v2.0/lb/vips'

        body = '{' \
       '"vip":{' \
        '"protocol": "HTTP",' \
        '"name": "' + vip_name + '",' \
        '"admin_state_up": "True",' \
        '"subnet_id": "' + subnet_id +'",' \
        '"pool_id": "' + pool_id + '",' \
        '"protocol_port": "80"' \
        '}' \
       '}'
        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid,'Content-Type':'application/json'}
        resp, rest_res = h.request(url, 'POST', headers=headers, body=str(body))

        print str(resp)
        print str(rest_res)

        return

    @classmethod
    def create_member(self,ops_base_obj,pool_id,target_ip):

        print "create member"

#        url = "http://192.168.99.225:9696/v2.0/lb/vips"

        url = 'http://'+ ops_base_obj.openstack_ip +':9696/v2.0/lb/members'

        body = '{' \
       '"member":{' \
        '"protocol_port": "80",' \
        '"pool_id": "' + pool_id + '",' \
        '"address": "' + target_ip + '",' \
        '"admin_state_up": "True"' \
        '}' \
       '}'
        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid,'Content-Type':'application/json'}
        resp, rest_res = h.request(url, 'POST', headers=headers, body=str(body))
        print str(resp)
        print str(rest_res)
        return