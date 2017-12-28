#! /usr/bin/python3
# coding=utf-8
'''
  name = clinet.py
'''


import socket


class client:

  def __init__(self, **kwargs):
    self.host = '127.0.0.1'
    self.port = 60013
    return super().__init__(**kwargs)

  def run(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
      self.sock.connect((self.host, self.port))
      self.sock.sendall(bytes('abc123ABC1456' + '\n', 'utf-8'))
      self.received = str(self.sock.recv(1024), 'utf-8')
    finally:
      self.sock.close()


def main():
  s=client()
  s.run()


if(__name__ == '__main__'):
  main();