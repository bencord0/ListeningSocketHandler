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
import socket
import sys
import threading
import unittest

class ListeningSocketHandler(logging.Handler):
    def __init__(self, port=0, ipv6=False):
        super(ListeningSocketHandler, self).__init__()
        if ipv6:
            a = socket.socket(socket.AF_INET6)
            a.bind(("::", port))
        else:
            a = socket.socket(socket.AF_INET)
            a.bind(("0.0.0.0", port))
        self._acceptor = a
        self._acceptor.listen(1)
        self._conn = None

        def start_listening(tsh):
            while True:
                try:
                    conn, addr = tsh._acceptor.accept()
                    tsh._conn = conn.makefile('w')
                except socket.error:
                    pass

        self._accept_thread = threading.Thread(target=start_listening, args=(self,))
        self._accept_thread.daemon = True
        self._accept_thread.start()

    def emit(self, record):
        if self._conn is None:
            # Silently drop the log
            return
        try:
            self._conn.write(record.getMessage())
            self._conn.write("\n")
            self._conn.flush()
        except socket.error:
            self._conn = None

    def flush(self):
        if self._conn:
            self._conn.flush()

    def getsockname(self):
        return self._acceptor.getsockname()

class TestListeningSocketHandler(unittest.TestCase):
    def setUp(self):
        self.log = logging.getLogger()
        # default will bind to any unsed port.
        self.lsh = ListeningSocketHandler()
        self.log.addHandler(self.lsh)

    def test_send_message(self):
        self.log.warn("Sending a warning")

    def test_getsockport(self):
        self.assertIsInstance(self.lsh.getsockname()[1], int)

    def test_recieve_message(self):
        client = socket.socket()
        client.connect(("localhost", self.lsh.getsockname()[1]))
        self.log.warn("Sending a warning")
        buf = client.recv(4096)
        self.assertEqual(buf, "Sending a warning\n")

if __name__ == '__main__':
    unittest.main()
