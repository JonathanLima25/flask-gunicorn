
def app(environ, start_response):
    #environ
    start_response('200 OK', [('Content_type', 'text/plain')])
    return [b'Hello wsGI']

