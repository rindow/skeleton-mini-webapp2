#!/usr/bin/env python
# coding: UTF-8
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'src'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vendor'))
import loader

from rindow.container.packagemanager import PackageManager
try:
    from config.settings import config
    packageMgr = PackageManager(config)
    app = packageMgr.getServiceLocator().get('webapp2.WSGIApplication')
    app.registry['serviceLocator'] = packageMgr.getServiceLocator()
except Exception, e:
    from rindow.stdlib.debug import MakeWsgiDump
    import traceback
    app = MakeWsgiDump(traceback.format_exc())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
