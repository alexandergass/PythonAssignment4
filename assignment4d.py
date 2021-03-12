import cgi;
from wsgiref.simple_server import make_server;

import xml.etree.ElementTree as etree;
tree = etree.parse('fav_movies.xml');
root = tree.getroot( );

html = """<table border="1" cellspacing="2">

        """

i = 0

for child in root.iter('title'):
    title = child.text
    for child in root.iter('year'):
        year = child.text

    if (i % 3 == 0):
        html += """<tr></tr>"""
    html2 = """<td><h1>%s(%s)<h1></td>
            
    """
    html += html2 % (title, year)

    i+=1

def app (environ, start_response):
    response = html;
    if ( environ['REQUEST_METHOD'] == "POST"):
        post_env = environ.copy();
        post_env["QUERY_STRING"] = "";

        post = cgi.FieldStorage(
            fp = environ["wsgi.input"],
            environ = post_env,
            keep_blank_values=True
        );

    start_response('200 OK', [('Content-Type','text/html')]);
    return [html.encode( )];

    cursor.close();
    db.close();

    import gc;
    gc.collect();

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server;
        httpd = make_server('', 8080, app);
        print('Serving on port 8080...');
        httpd.serve_forever();
    except KeyboardInterrupt:
        print("Goodbye");