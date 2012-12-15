#!/usr/bin/env python
"""
    ListeningSocketHandler
    ======================
    A python logging handler.
    logging.handlers.SocketHandler is a TCP Socket client that sends log records to a tcp server.
    This class is the opposite.
    When a TCP client connects (e.g. telnet or netcat), log records are streamed through the connection.
"""

import logging
import sys

import socket
import threading

# Workaround for http://bugs.python.org/issue14308
# http://stackoverflow.com/questions/13193278/understand-python-threading-bug
threading._DummyThread._Thread__stop = lambda x: 42

class ListeningSocketHandler(logging.Handler):
    def __init__(self, port=0, ipv6=False):
        super(ListeningSocketHandler, self).__init__()
        self.port = port
        self.ipv6 = ipv6
        self.clients = set()
        if self.ipv6:
            self.socket = socket.socket(socket.AF_INET6)
            self.socket.bind(("::", self.port))
        else:
            self.socket = socket.socket(socket.AF_INET)
            self.socket.bind(("0.0.0.0", self.port))
        self.socket.listen(5)
        print ("ListeningSocketHandler on port: {}".format(self.socket.getsockname()[1]))
        def start_accepting(self):
            while True:
                    conn, addr = self.socket.accept()
                    self.clients.add(conn)

        self._accept_thread = threading.Thread(target=start_accepting, args=(self,))
        self._accept_thread.daemon = True
        self._accept_thread.start()

    def emit(self, record):
        closed_clients = set()
        for client in self.clients:
            try:
                try:
                    # Python3
                    message = bytes(record.getMessage() + "\r\n", 'UTF-8')
                except TypeError:
                    # Python2
                    message = bytes(record.getMessage() + "\r\n").encode('UTF-8')
                client.sendall(message)
            except socket.error:
                closed_clients.add(client)
        for client in closed_clients:
            client.close() # just to be sure
            self.clients.remove(client)

    def getsockname(self):
        return self.socket.getsockname()

