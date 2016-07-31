# coding: utf-8

from oslo_config import cfg, types

CONF = cfg.CONF
PortType = types.Integer(1, 65535)


openstack_sample_opts = [
    cfg.StrOpt('bind_host',
               default='0.0.0.0',
               help='IP address to listen on'),
    cfg.Opt('bind_port',
            type=PortType,
            default=9292,
            help='Port number to listen on'),
]

CONF.register_opts(openstack_sample_opts, 'openstack_sample')


def list_opts():
    return {
        'openstack_sample': openstack_sample_opts,
    }
