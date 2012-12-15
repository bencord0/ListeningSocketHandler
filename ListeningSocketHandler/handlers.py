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

import eventlet
from eventlet.green import socket, threading

class ListeningSocketHandler(logging.Handler):
    def __init__(self, port=0, ipv6=False):
        super(ListeningSocketHandler, self).__init__()
        self.port = port
        self.ipv6 = ipv6
        self.clients = set()
        if self.ipv6:
            self.socket = eventlet.listen(
                ("::", self.port),
                socket.AF_INET6)
        else:
            self.socket = eventlet.listen(
                ("0.0.0.0", self.port),
                socket.AF_INET)
        def start_listening(self):
            while True:
                    conn, addr = self.socket.accept()
                    self.clients.add(conn)

        self._accept_thread = threading.Thread(
            target=start_listening,
            args=(self,))
        self._accept_thread.daemon = True
        self._accept_thread.start()

    def emit(self, record):
        closed_clients = set()
        for client in self.clients:
            try:
                client.sendall(record.getMessage())
                client.sendall("\n")
            except socket.error:
                closed_clients.add(client)
        for client in closed_clients:
            client.close() # just to be sure
            self.clients.remove(client)

    def getsockname(self):
        return self.socket.getsockname()

