config = {
    'package_manager': {
        'packages': [
            'rindow.bridge.google.appengine',
            'acme.greeting',
            'acme.debug',
        ]
        #'use_global_container': True
    },
    'container': {
        'components': {
            'webapp2.WSGIApplication': {
                'construct_args': {
                    'debug':  { 'value': True },
                }
            }
        }
    }
}
