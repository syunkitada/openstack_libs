# coding: utf-8

import itertools
from oslo_config import cfg, types

CONF = cfg.CONF
PortType = types.Integer(1, 65535)


openstack_sample_opts = [
    cfg.StrOpt('topic',
               default='openstack_sample',
               help='topic'),
    cfg.StrOpt('host',
               default='localhost',
               help='host'),
    cfg.StrOpt('bind_host',
               default='127.0.0.1',
               help='IP address to listen on'),
    cfg.Opt('bind_port',
            type=PortType,
            default=8080,
            help='Port number to listen on'),
]


def list_opts():
    return [
        ('openstack_sample', itertools.chain(openstack_sample_opts))
    ]
