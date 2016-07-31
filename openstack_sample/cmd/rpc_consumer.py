# coding: utf-8

from openstack_sample.conf import config
from openstack_sample.service import rpc_consumer


def main():
    config.init()
    rpc_consumer.launch()
