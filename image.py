from PIL import Image
import pytesseract
import dotenv
import os

# Tesseractのインストールパスを指定
pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH")

def transcription(path: str):

    # 画像の読み込み
    image_path = path
    image = Image.open(image_path)

    text = pytesseract.image_to_string(image, lang='eng')

    return text

