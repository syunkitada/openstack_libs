# coding: utf-8

from oslo_config import cfg
from oslo_log import log as logging
import oslo_messaging
from oslo_service import service

CONF = cfg.CONF
LOG = logging.getLogger(__name__)


class ServerControlEndpoint(object):
    target = oslo_messaging.Target(namespace='control',
                                   version='2.0')

    def __init__(self, server):
        self.server = server

    def stop(self, ctx):
        if self.server:
            self.server.stop()


class TestEndpoint(object):
    target = oslo_messaging.Target(version='2.0')

    def test(self, ctx, arg):
        LOG.info('DEBUG')
        return arg


class Consumer(service.Service):

    def __init__(self):
        super(Consumer, self).__init__()
        self.server = None

    def start(self):
        transport = oslo_messaging.get_transport(CONF)
        target = oslo_messaging.Target(topic=CONF.openstack_sample.topic,
                                       server=CONF.openstack_sample.host)
        endpoints = [
            ServerControlEndpoint(None),
            TestEndpoint(),
        ]
        self.server = oslo_messaging.get_rpc_server(
            transport, target, endpoints, executor='threading')

        self.server.start()

        super(Consumer, self).start()

    def stop(self, graceful=False):
        if self.server:
            LOG.info('Stopping consumer...')
            self.server.stop()
            if graceful:
                LOG.info('Consumer successfully stopped.  Waiting for final '
                         'messages to be processed...')
                self.server.wait()
        super(Consumer, self).stop(graceful=graceful)

    def reset(self):
        if self.server:
            self.server.reset()
        super(Consumer, self).reset()


def launch():
    launcher = service.launch(CONF, Consumer())
    launcher.wait()
