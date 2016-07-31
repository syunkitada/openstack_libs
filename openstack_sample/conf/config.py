# coding: utf-8

from oslo_config import cfg
from oslo_log import log
from openstack_sample.conf import constant, opts

LOG = log.getLogger(__name__)

CONF = cfg.CONF
CONF.register_opts(opts.openstack_sample_opts, 'openstack_sample')


def init():
    log.register_options(CONF)
    CONF([], default_config_files=[constant.INIFILE])
    log.setup(CONF, constant.LOG_DOMEIN)
    LOG.info('init conf')
