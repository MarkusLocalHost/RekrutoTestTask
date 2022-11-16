from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        name = parse.parse_qs(parse.urlparse(self.path).query).get("name")
        message = parse.parse_qs(parse.urlparse(self.path).query).get("message")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        try:
            self.wfile.write(
                b'Hello ' + name[0].encode(encoding="UTF-8") + b'! ' + message[0].encode(encoding="UTF-8") + b'!')
        except:
            self.wfile.write(
                b'Sorry, you didnt enter name or message...')


def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


if __name__ == "__main__":
    run()
