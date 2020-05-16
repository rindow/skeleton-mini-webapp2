import os

config = {
    'mvc': {
        'router': {
            'routings': [
                ('/', 'acme.greeting.controller.main.MainHandler'),
                ('/sign', 'acme.greeting.controller.main.Guestbook')
            ],
        },
        'view': {
            'template_paths':[
                os.path.dirname(__file__) + '/../views'
            ]
        }
    },
    'container': {
        'aliases': {
            'template': 'rindow.bridge.google.appengine.jinja2.DefaultEnvironment',
            'greeting': 'acme.greeting.greetingManager'
        },
        'components': {
            'acme.greeting.greetingManager': {
                'class': 'acme.greeting.model.dao.GreetingManager'
            }
        }
    }
}
