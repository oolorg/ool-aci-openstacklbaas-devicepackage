#from django.http import JsonResponse
import sys
import httplib2
import json
from openstack_base import openstack_base


class neutron:

    result_json = {}
    server_all_info = {}

    @classmethod
    def getlist(self,ops_base_obj):

        print "get network info"
        url = 'http://'+ops_base_obj.openstack_ip+':9696/v2.0/networks'
        body = ''
        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid}
        resp, token = h.request(url, 'GET', headers=headers, body=body)
        token_body_byt = token
        toke_body = token_body_byt.decode(sys.stdin.encoding)
        self.server_all_info = json.loads(toke_body)

    @classmethod
    def get_subnet_id(self,ops_base_obj,subnet_name):

        print "get subnet list"
        url = 'http://'+ops_base_obj.openstack_ip+':9696/v2.0/subnets'
        body = ''
        h = httplib2.Http(timeout=30)
        headers = {'X-Auth-Token': ops_base_obj.tokenid}
        resp, rest_res = h.request(url, 'GET', headers=headers, body=body)
        token_body_byt = rest_res
        toke_body = token_body_byt.decode(sys.stdin.encoding)
        self.server_all_info = json.loads(toke_body)
        subnet_id = ""
        for subnets_list in self.server_all_info['subnets']:
            if str(subnets_list['name']) == str(subnet_name):
                subnet_id = str(subnets_list['id'])
                break

        print rest_res

        return subnet_id


        return
