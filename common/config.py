# coding: utf-8

from oslo_config import cfg
from oslo_config import types
import oslo_messaging

PortType = types.Integer(1, 65535)

core_opts = [
    cfg.StrOpt('bind_host',
               default='0.0.0.0',
               help='IP address to listen on'),
]

core_cli_opts = [
    cfg.Opt('bind_port',
            type=PortType,
            default=9292,
            help='Port number to listen on'),
]

cfg.CONF.register_opts(core_opts)
cfg.CONF.register_cli_opts(core_cli_opts)
cfg.CONF(default_config_files=['etc/common.conf'])

oslo_messaging.set_transport_defaults(control_exchange='neutron')
