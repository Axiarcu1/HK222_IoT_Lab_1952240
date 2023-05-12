import sys
import unittest
from unittest.mock import MagicMock
from main import *
from uart import *

class TestMQTTClient(unittest.TestCase):

    def setUp(self):
        self.client = MagicMock()
        self.client.subscribe = MagicMock()
        self.client.publish = MagicMock()


    def test_connected(self):
        connected(self.client)
        self.assertEqual(self.client.subscribe.call_count, 2)



    def test_subscribe(self):
        subscribe(self.client, None, None, None)
        self.assertTrue(True) # nothing to test here, just check that it doesn't crash


    def test_disconnected(self):
        with self.assertRaises(SystemExit):
            disconnected(self.client)

    # def test_message_nut_nhan_1(self):
    #     message(self.client, 'nut-nhan-1', '0')
    #     self.client.publish.assert_called_once_with('serial', '1')
    #     self.client.publish.reset_mock()
    #     message(self.client, 'nut-nhan-1', '1')
    #     self.client.publish.assert_called_once_with('serial', '2')



if __name__ == '__main__':
    unittest.main(exit=False)
