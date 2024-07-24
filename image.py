from PIL import Image
import pyautogui as pg
import pytesseract
import cv2
import numpy as np

# Tesseractのインストールパスを指定
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def transcription(path: str):

    # 画像の読み込み
    image_path = path
    image = Image.open(image_path)

    text = pytesseract.image_to_string(image, lang='eng')

    return text

def find_image_on_screen(template_path, threshold=0.8):

    # 初項0.1,末項5.0,公差0.1の等差数列
    scales = np.arange(0.1, 5.1, 0.1)
    # 画面のスクリーンショットを取得し、OpenCVの形式に変換
    screenshot = pg.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # テンプレート画像を読み込む
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    
    for scale in scales:
        # テンプレート画像をスケールに応じてリサイズ
        resized_template = cv2.resize(template, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        
        # テンプレートマッチングを実行
        result = cv2.matchTemplate(screenshot, resized_template, cv2.TM_CCOEFF_NORMED)
        
        # 一致度が閾値以上の位置を取得
        loc = np.where(result >= threshold)
        
        if len(loc[0]) > 0:
            # 最初に見つかった一致位置を返す
            pt = loc[1][0], loc[0][0]
            return [pt[0], pt[1], pt[0] + resized_template.shape[1], pt[1] + resized_template.shape[0], scale]
    
    # 一致する画像が見つからない場合
    return None

