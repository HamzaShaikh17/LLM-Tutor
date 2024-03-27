from PIL import Image
import pytesseract
import numpy as np

filename = './question.PNG'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

# pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'  # your path may be different

print(text)