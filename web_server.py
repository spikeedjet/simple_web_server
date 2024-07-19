# Corrected imports for Python 3

import http.server  # Use http.server for Python 3 (BaseHTTPServer deprecated)
import os


PORT = 8080  # Define server port

class ServerException(Exception):
    def __init__(self, message):
        super().__init__(message)



class RequestHandler(http.server.BaseHTTPRequestHandler):
#     """Handle HTTP requests by returning a fixed 'Hello, web!' page."""
    # Page to send back
    Page = """\
<html>
<body>
<table>
<tr>    <td>Header</td>             <td>Value</td>              </tr>
<tr>    <td>Date and time</td>      <td>{date_time}</td>        </tr>
<tr>    <td>Client host</td>        <td>{client_host}</td>      </tr>
<tr>    <td>Client port</td>        <td>{client_port}</td>      </tr>
<tr>    <td>Command</td>            <td>{command}</td>          </tr>
<tr>    <td>Path</td>               <td>V{path}</td>            </tr>
</table>
</body>
</html>
"""

    Error_Page ="""\
<html>
<body>
<h1>Error acessing {path}</h1>
<p>{msg}</p>
</body>
</html>
"""
    def handle_error(self,msg):
        content = self.Error_Page.format(path=self.path,msg=msg)
        self.send_content(content,404)

    def send_content(self,content,status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)  # Encode content as bytes


    def do_GET(self):
        # page = self.create_page()
        # self.send_page(page)
        try :
            #figure out what exatly is being requested
            full_path = os.getcwd() + self.path

            #It doesn't exist...
            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))

            #It's a file
            elif os.path.isfile(full_path):
                self.handle_file(full_path)

            # ...it's something we don't handle
            else:
                raise ServerException("Unknow object'{0}'".format(self.path))

        except Exception as msg:
            self.handle_error(msg)

    def handle_file (self,full_path):
        try:
            with open(full_path,'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except Exception as msg:
            msg = "'{0}' cannot be read:{1}".format(self.path,msg)
            self.handle_error(msg)

    def create_page(self):
        values = {
            'date_time'     :   self.date_time_string(),
            'client_host'   :   self.client_address[0],
            'client_port'   :   self.client_address[1],
            'command'       :   self.command,
            'path'          :   self.path
        }
        page = self.Page.format(**values)
        return page

    def send_page(self,page):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("Content-Length",str(len(page)))
        self.end_headers()
        self.wfile.write(page.encode('utf-8'))


def main():
    """Start the simple HTTP server."""
    server_address = ('', PORT)
    server = http.server.HTTPServer(server_address, RequestHandler)
    print(f"Serving at port {PORT}")
    server.serve_forever()

if __name__ == '__main__':
    main()
