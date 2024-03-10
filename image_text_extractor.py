import easyocr
from io import BytesIO


def extract(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path, detail=0)
    return result[0]


def web_extract(file):
    file.seek(0)

    # Load the file into memory using BytesIO
    file_buffer = BytesIO(file.read())

    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_buffer, detail=0)
    return result[0]
