import context
from context import unittest

class FileHashTest(unittest.TestCase):

    def test_get_file(self):
        test_file_path = '../assets/images/panda-test-image.png'
        result = 