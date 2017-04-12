#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

from OpenstackLib.OpenstackLbaasConfig import OpenstackLbaasConfig


__author__ = 'Fabrice Servais'

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))


# Device
def deviceValidate(device, version):
    return return_ok()


def deviceAudit(device, interfaces, configuration):
    return return_ok()


def deviceModify(device, interfaces, configuration):
    return return_ok()



def deviceHealth(device, interfaces, configuration):
    return return_ok()


def deviceCounters(device, interfaces, configuration):
    print ""
    return return_ok()


#
# Clusters
def clusterAudit(device, interfaces, configuration):
    print ""
    return return_ok()


def clusterModify(device, interfaces, configuration):
    return return_ok()


#
# Services
def serviceAudit(device, configuration):


    ops_lb = OpenstackLbaasConfig()

    #ops_lb.username = configuration.get('op_user')
    #ops_lb.password = configuration.get('op_password')
    #ops_lb.openstack_ip = configuration.get('op_ip')
    #ops_lb.lb_pool_name = configuration.get('pool_name')
    #ops_lb.lb_vip_name = configuration.get('vip_name')
    #ops_lb.subnet_name = configuration.get('subnet_name')
    ops_lb.init()
    ops_lb.create_lb()
    ops_lb.create_member('192.168.1.15')
    ops_lb.create_member('192.168.1.18')


    #return return_ok()


def serviceModify(device, configuration):
    return return_ok()


def serviceHealth(device, configuration):
    return return_ok()


def serviceCounters(device, configuration):
    return return_ok()


def attachEndpoint(device, configuration, endpoints):
    return return_ok()


def detachEndpoint(device, configuration, endpoints):
    return return_ok()


def attachNetwork(device, configuration, connector, networks):
    return return_ok()


def detachNetwork(device, configuration, connector, networks):
    return return_ok()


# Misc. functions
def return_ok(score=100):
    return 0

def return_transient(health_score=100, faults=[]):
    return 1
