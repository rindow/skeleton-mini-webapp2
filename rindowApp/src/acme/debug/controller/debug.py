import webapp2
import os,jinja2
from google.appengine.api import users
import gc

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'..','views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def dump_garbage():
    gc.collect()
    result = ''
    i = 0
    for x in gc.garbage:
        s = str(x)
        if len(s) > 80: s = s[:77]+'...'
        result = result + type(x).__name__ + '\n ' + s + '\n'
        i = i + 1
    result = ('GARBAGE OBJECTS: total %d\n' % i) + result
    return result

def dump_object():
    gc.collect()
    result = ''
    i = 0
    objects = gc.get_objects()
    types = {}
    for x in objects:
        #s = str(x)
        #if len(s) > 80: s = s[:77]+'...'
        typename = type(x).__name__
        #result = result + typename + '\n'# + s + '\n'
        i = i + 1
        types[typename] = types.get(typename,0) + 1
        #if (i % 500)==0 :
        #    result = result + 'count=%d\n' % i
    typelist = []
    for (typename,typecount) in types.iteritems() :
        typeinfo = { 'name': typename, 'count': typecount }
        typelist.append(typeinfo)
    typelist.sort(lambda x,y: y['count'] - x['count'])
    for typeinfo in typelist :
        result = result + '%s : %d\n' % (typeinfo['name'],typeinfo['count'])
    result = ('OBJECTS: total %d\n' % i) + result
    if gc.isenabled() :
        result = 'auto colection: enable\n' + result
    else :
        result = 'auto colection: disable\n' + result
    return result

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        if not users.is_current_user_admin():
            self.redirect('/')
            return
        super(BaseHandler, self).dispatch()

    def render_response(self, _filename, **context):
        # Renders a template and writes the result to the response.
        #template = self.serviceLocator.get('rindow.cms.pages.template').get_template(_filename)
        template = JINJA_ENVIRONMENT.get_template(_filename)
        self.response.write(template.render(context))
 
class DumpGarbage(BaseHandler):
    def get(self):
        debug = dump_garbage()
        self.render_response('debug.html',
            debug=debug
        )
 
class DumpObject(BaseHandler):
    def get(self):
        debug = dump_object()
        self.render_response('debug.html',
            debug=debug
        )
