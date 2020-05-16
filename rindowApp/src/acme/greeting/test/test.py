import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../src')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../vendor')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')

import unittest
from config.settings import config
from rindow.container.container import GetGlobalContainer

container = GetGlobalContainer(config['container'])
print container.componentManager.config
print container.componentManager.has('builder')