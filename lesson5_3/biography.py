import wsgiref


def start_response(param, headers):
    pass


def application(environ, start_reaponse):
    headers = [('Content-Type', 'text/html; charset = utf-8')]
    start_response('200 OK', headers)

    path = environ['PATH_INFO']
    if path == '/biography':
        page = '''<!DOCTYPE html>
        <html><head><title>Biography</title></head><body>
        <h1>Hi, I'm Umika Ooka</h1>
        <h2>About me</h2>
        <p>I am 16 years old. I am currently a sophomore in a high school in Brooklyn.</p>
        <p>I do ice skating. I started when I was 3.</p>
        <p>I like to bake.</p>
        <a href = https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/>One of my favorite recipe</a>
        <br />
        </body>
        </html>'''

    return [page.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()