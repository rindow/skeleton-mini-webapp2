import webapp2
import urllib

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        self.serviceLocator = self.app.registry.get('serviceLocator')
        self.greetingManager = self.serviceLocator.get('greeting')
        super(BaseHandler,self).dispatch()

    def render_response(self, _filename, **context):
        template = self.serviceLocator.get('template').get_template(_filename)
        self.response.write(template.render(context))

class MainHandler(BaseHandler):
    def get(self):
        guestbook_name = self.request.params.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        self.render_response('index.html',
            greetings = self.greetingManager.list(guestbook_name),
            guestbook_name = urllib.quote_plus(guestbook_name)
            )

class Guestbook(BaseHandler):
    def post(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        content = self.request.get('content')
        nickname = self.request.get('nickname',None)
        email = self.request.get('email',None)
        self.greetingManager.add(guestbook_name,content,nickname,email)
        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/?' + urllib.urlencode(query_params))
