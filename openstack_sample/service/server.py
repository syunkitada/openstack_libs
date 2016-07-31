# coding: utf-8

import threading
from oslo_config import cfg
from oslo_log import log
from oslo_service import service

CONF = cfg.CONF
LOG = log.getLogger(__name__)


class APIService(service.Service):
    def __init__(self, name='openstack_sample'):
        super(APIService, self).__init__()

    def start(self):
        LOG.info('start')
        self.udp_thread = self.spawn_app()

    def wait(self):
        LOG.info('wait')

    def stop(self):
        LOG.info('stop')

        if self.udp_thread:
            self.udp_thread.join()

        super(APIService, self).stop()

    def spawn_app(self):
        # t = threading.Thread(target=wsgi_app.run, args=args, kwargs=kwargs)
        from wsgi_app import wsgi_app

        t = threading.Thread(target=wsgi_app.run, kwargs={
            'host': CONF.openstack_sample.bind_host,
            'port': CONF.openstack_sample.bind_port
        })
        t.daemon = True
        t.start()
        return t


def launch():
    launcher = service.launch(CONF, APIService())
    launcher.wait()
