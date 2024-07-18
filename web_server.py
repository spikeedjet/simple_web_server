# Corrected imports for Python 3

import http.server  # Use http.server for Python 3 (BaseHTTPServer deprecated)

PORT = 8080  # Define server port

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

#     def do_GET(self):
#         """Handle GET requests."""
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.send_header("Content-Length", str(len(self.Page)))
#         self.end_headers()
#         self.wfile.write(self.Page.encode('utf-8'))  # Encode content as bytes
    # page template
    def do_GET(self):
        page = self.create_page()
        self.send_page(page)

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
