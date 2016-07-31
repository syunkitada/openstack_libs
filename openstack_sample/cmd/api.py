# coding: utf-8

from openstack_sample.conf import config
from openstack_sample.service import server_consumer


def main():
    config.init()
    server_consumer.launch()
