import unittest
from media2nft.converters import FileHasher


class FileHashTest(unittest.TestCase):

    def test_get_file(self):
        test_file_path = './assets/images/panda-test-image.png'
        result = FileHasher.get_file(test_file_path)
        self.assertIsNotNone(self, result)

    def test_compute_md5(self):
        test_file_path = './assets/images/panda-test-image.png'
        try:
            with open(test_file_path, 'rb') as test_file:
                file_content = test_file.read()
                test_md5_result = FileHasher.compute_md5(file_content)
                self.assertEqual(test_md5_result, '55535d04f79206b37deac90d22bb7762')
        except RuntimeError:
            raise RuntimeError('Failure while attempting to read file')

    def test_get_codec(self):
        test_file_extension_1 = '.mp4'
        test_file_extension_2 = '.jpeg'
        test_file_extension_3 = 'PNG'
        test_file_extension_4 = 'gif'
        test_file_extension_5 = 'mp3'
        test_file_extension_6 = '.FLAC'

        result_1 = FileHasher.get_codec(test_file_extension_1)
        result_2 = FileHasher.get_codec(test_file_extension_2)
        result_3 = FileHasher.get_codec(test_file_extension_3)
        result_4 = FileHasher.get_codec(test_file_extension_4)
        result_5 = FileHasher.get_codec(test_file_extension_5)
        result_6 = FileHasher.get_codec(test_file_extension_6)

        self.assertEqual(result_1, 'video/mp4')
        self.assertEqual(result_2, 'image/jpeg')
        self.assertEqual(result_3, 'image/png')
        self.assertEqual(result_4, 'image/gif')
        self.assertEqual(result_5, 'audio/mpeg')
        self.assertEqual(result_6, 'audio/flac')
