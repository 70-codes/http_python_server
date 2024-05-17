from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "192.168.8.2"
PORT = 8000


class NerualHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(
            bytes("<html><body><h1>Hello World</h1></body></html>", "utf-8")
        )
        pass

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time":"%s"}\n' % date, "utf-8"))
        pass


def main():
    server = HTTPServer((HOST, PORT), NerualHTTP)
    print("Server started http://%s:%s" % (HOST, PORT))
    server.serve_forever()
    server.server_close()
    print("Server stopped.")


if __name__ == "__main__":
    main()
