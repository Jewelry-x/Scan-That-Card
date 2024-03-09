import easyocr


def extract(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext("cards/wildedge.jpg", detail=0)
    return result[0]
