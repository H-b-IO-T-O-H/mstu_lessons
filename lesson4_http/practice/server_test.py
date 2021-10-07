import json
import unittest
from multiprocessing import Process

import requests

from http_server import Server

class MyTestCase(unittest.TestCase):
    def test_hello(self):
        resp = requests.get('http://localhost:8080').json()
        self.assertEqual(resp, {'status': 200, 'content': 'Hello world!'})


if __name__ == '__main__':
    unittest.main()
