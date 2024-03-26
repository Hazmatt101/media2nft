import mimetypes


class CustomMimetypes:
    @staticmethod
    def __init__():
        mimetypes.add_type('audio/flac', '.flac')
        mimetypes.add_type('image/png', '.png')

    @staticmethod
    def get_mimetype(file_extension):
        CustomMimetypes.__init__()
        if not file_extension.startswith('.'):
            file_extension = '.' + file_extension
        return mimetypes.types_map.get(file_extension.lower())
