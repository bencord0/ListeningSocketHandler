import logging
import threading
import unittest

try:
    from gevent import socket, Greenlet
except ImportError:
    import socket
    import threading

from ListeningSocketHandler import ListeningSocketHandler

class BasicTests(unittest.TestCase):
    def test_ipv4(self):
        lsh4 = ListeningSocketHandler(ipv6=False)
        self.assertIsInstance(lsh4.getsockname()[1], int)
    
    def test_ipv6(self):
        lsh6 = ListeningSocketHandler(ipv6=True)
        self.assertIsInstance(lsh6.getsockname()[1], int)
    
class TestListeningSocketHandler(unittest.TestCase):
    def setUp(self):
        self.log = logging.getLogger('testlisteningsockethandler')
        #self.log.setLevel(logging.DEBUG)
        # default will bind to any unsed port.
        self.lsh = ListeningSocketHandler()
        #self.lsh.setLevel(logging.DEBUG)
        self.log.addHandler(self.lsh)

    def _send_message(self):
        self.log.debug("Sending debugging")
        self.log.info("Sending information")
        self.log.warn("Sending a warning")
        self.log.error("Sending an error")
        self.log.critical("Exploding")

    def test_send_message(self):
        self._send_message()

    def test_recv_message(self):
        port = self.lsh.getsockname()[1]
        recv_buf = ""

        def start_receiving(port, recv_buf):
            c = socket.create_connection(("localhost", port), 5)
            recv_buf = c.recv(2048)
            c.close()
            self.assertEquals(recv_buf,
"""Sending a warning
Sending an error
Exploding
""")

        try:
            receiving_thread = Greenlet(start_receiving, port, recv_buf)
        except NameError:
            receiving_thread = threading.Thread(target=start_receiving, args=(port, recv_buf))
            receiving_thread.daemon=True
        receiving_thread.start()
        self._send_message()

if __name__ == '__main__':
    unittest.main()
