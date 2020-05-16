import webapp2
from acme.debug.controller.debug import DumpGarbage
from acme.debug.controller.debug import DumpObject
config = {
    'mvc': {
        'router': {
            'routings': [
                webapp2.Route(r'/dumpgarbage', handler=DumpGarbage, name='dumpgarbage'),
                webapp2.Route(r'/dumpobject', handler=DumpObject, name='dumpobject'),
            ],
        },
        #'view': {
        #    'template_paths':[
        #        os.path.dirname(__file__) + '/../views'
        #    ]
        #}
    }
}