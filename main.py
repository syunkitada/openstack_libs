#!/usr/bin/env python
# coding: utf-8

from oslo_config import cfg
from common import config


if __name__ == '__main__':
    print 'main'
    print cfg.CONF.bind_host
    print cfg.CONF.bind_port
