import logging
import socket
import unittest

from ListeningSocketHandler import ListeningSocketHandler

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

if __name__ == '__main__':
    unittest.main()
