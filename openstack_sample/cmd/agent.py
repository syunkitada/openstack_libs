# coding: utf-8

from openstack_sample.conf import config
from openstack_sample.service import agent


def main():
    config.init()
    agent.launch()
