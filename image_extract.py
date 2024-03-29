from PIL import Image
import pytesseract
import numpy as np

def image_text(filename):
    #filename = './question.PNG'
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1)
    return text


