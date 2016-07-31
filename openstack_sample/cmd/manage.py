# coding: utf-8

import oslo_messaging
from oslo_config import cfg
from openstack_sample.conf import config

CONF = cfg.CONF


def main():
    config.init()
    transport = oslo_messaging.get_transport(CONF)
    target = oslo_messaging.Target(
        topic=CONF.openstack_sample.topic + '.localhost', version='2.0')
    client = oslo_messaging.RPCClient(transport, target)
    print client.call({'some': 'context'}, 'test', arg='hello')
