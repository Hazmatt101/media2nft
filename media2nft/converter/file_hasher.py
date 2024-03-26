import hashlib
from custom_mimetypes import custom_mimetypes


class FileHasher:
    @staticmethod
    def get_file(file_path):
        try:
            with open(file_path, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError("File not found. Check filepath.")

    @staticmethod
    def get_codec(file_extension):
        if not file_extension.startswith('.'):
            file_extension = '.' + file_extension
        mime_type = custom_mimetypes.CustomMimetypes.get_mimetype(file_extension)
        if mime_type is None:
            return f"No codec found for the file extension {file_extension}"
        return mime_type

    @staticmethod
    def compute_md5(file_content):
        try:
            md5_hash = hashlib.md5()
            md5_hash.update(file_content)
            return md5_hash.hexdigest()
        except RuntimeError:
            return "Failed to compute MD5 hash for file"

