# coding: utf-8

import oslo_messaging
from oslo_config import cfg
from flask import Flask
wsgi_app = Flask(__name__)

CONF = cfg.CONF


transport = oslo_messaging.get_transport(CONF)
target = oslo_messaging.Target(
    topic=CONF.openstack_sample.topic, version='2.0')
client = oslo_messaging.RPCClient(transport, target)


@wsgi_app.route("/")
def hello():
    print client.call({'some': 'context'}, 'test', arg='hello')
    return "Hello World!"
