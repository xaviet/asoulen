#! /usr/bin/python3
# coding=utf-8
'''
  name = server.py
'''


import socketserver


class handler(socketserver.BaseRequestHandler):
 
    def handle(self):
        self.data = self.request.recv(2048).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())


class server:

  def __init__(self, **kwargs):
    self.host = '0.0.0.0'
    self.port = 60013
    return super().__init__(**kwargs)

  def run(self):
    self.sock = socketserver.TCPServer((self.host, self.port), handler)
    self.sock.serve_forever()


def main():
  s=server()
  s.run()


if(__name__ == '__main__'):
  main();
