# coding: utf-8

from oslo_config import cfg
from oslo_log import log as logging
import oslo_messaging as messaging

CONF = cfg.CONF
LOG = logging.getLogger(__name__)


class RPCClient():

    def __init__(self):
        transport = messaging.get_transport(CONF)
        target = messaging.Target(topic=CONF.openstack_sample.topic)
        self.client = messaging.RPCClient(transport, target)

    def test(self):
        LOG.info('test')
        self.client.cast({}, 'debug', arg='hello')
