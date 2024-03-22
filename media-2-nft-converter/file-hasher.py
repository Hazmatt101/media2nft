import hashlib

class FileHasher:
    def get_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                return file
        except FileNotFoundError:
            raise FileNotFoundError("File not found. Check filepath.") 


    def get_file_contents(self, file):
        try:
            return file.read()
        except IOError:
            raise IOError("Could not read file.")


    def compute_md5(self, file_content):
        try:
            md5_hash = hashlib.md5(file_content).hexdigest()
            return md5_hash
        except RuntimeError:
            return "Failed to compute MD5 hash for file"