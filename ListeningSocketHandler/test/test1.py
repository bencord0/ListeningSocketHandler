import logging
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

    def test_recieve_message(self):
        client = socket.socket()
        client.connect(("localhost", self.lsh.getsockname()[1]))
        self.log.warn("Sending a warning")
        buf = client.recv(4096)
        self.assertEqual(buf, "Sending a warning\n")

if __name__ == '__main__':
    unittest.main()
