from PIL import Image
import pyautogui as pg
import pytesseract
import cv2
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_PATH')

def transcription(path: str):

    image_path = path
    image = Image.open(image_path)

    text = pytesseract.image_to_string(image, lang='eng')

    return text

def find_image_on_screen(template_path, threshold=0.8):

    scales = np.arange(0.1, 5.1, 0.1)
    screenshot = pg.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    
    for scale in scales:
        resized_template = cv2.resize(template, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        
        result = cv2.matchTemplate(screenshot, resized_template, cv2.TM_CCOEFF_NORMED)
        
        loc = np.where(result >= threshold)
        
        if len(loc[0]) > 0:
            pt = loc[1][0], loc[0][0]
            return [pt[0], pt[1], pt[0] + resized_template.shape[1], pt[1] + resized_template.shape[0], scale]
    
    return None

