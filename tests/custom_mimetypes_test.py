import unittest
from custom_mimetypes.custom_mimetypes import CustomMimetypes


class CustomMimetypesTest(unittest.TestCase):

    def test_get_mimetype(self):
        test_file_extension_1 = '.mp4'
        test_file_extension_2 = '.jpeg'
        test_file_extension_3 = 'PNG'
        test_file_extension_4 = 'gif'
        test_file_extension_5 = 'mp3'
        test_file_extension_6 = '.FLAC'

        mimetype_1 = CustomMimetypes.get_mimetype(test_file_extension_1)
        mimetype_2 = CustomMimetypes.get_mimetype(test_file_extension_2)
        mimetype_3 = CustomMimetypes.get_mimetype(test_file_extension_3)
        mimetype_4 = CustomMimetypes.get_mimetype(test_file_extension_4)
        mimetype_5 = CustomMimetypes.get_mimetype(test_file_extension_5)
        mimetype_6 = CustomMimetypes.get_mimetype(test_file_extension_6)

        self.assertEqual(mimetype_1, 'video/mp4')
        self.assertEqual(mimetype_2, 'image/jpeg')
        self.assertEqual(mimetype_3, 'image/png')
        self.assertEqual(mimetype_4, 'image/gif')
        self.assertEqual(mimetype_5, 'audio/mpeg')
        self.assertEqual(mimetype_6, 'audio/flac')