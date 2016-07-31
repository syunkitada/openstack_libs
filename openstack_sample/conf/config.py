# coding: utf-8

from oslo_config import cfg
from oslo_log import log
from openstack_sample.conf import constant

CONF = cfg.CONF
LOG = log.getLogger(__name__)


def init():
    CONF([], default_config_files=[constant.INIFILE])
    log.register_options(CONF)
    log.setup(CONF, constant.LOG_DOMEIN)
    LOG.info('init conf')
