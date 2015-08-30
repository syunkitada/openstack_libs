#!/usr/bin/env python
# coding: utf-8

from oslo_config import cfg
from common import config
import oslo_messaging as messaging


transport = messaging.get_transport(cfg.CONF)
target = messaging.Target(topic='test', version='2.0')
client = messaging.RPCClient(transport, target)
print client.call({'some': 'context'}, 'test', arg='hello')
