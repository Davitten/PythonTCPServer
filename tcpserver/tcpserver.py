import socketserver
from protos import addressbook_pb2


class TCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        data = self.rfile.readline().strip()
        print(f"Received data from host: {self.client_address[0]}:")
        print(data)
        # a = addressbook_pb2.Person()
        # print(a.ParseFromString(data))
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(data.upper())


class TCPServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        with socketserver.TCPServer((host, port), TCPHandler) as server:
            print(f"Started server with host:'{self.host}' on port: '{self.port}'")
            server.serve_forever()
