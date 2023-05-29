import pytesseract
import sys
import argparse

path = 'e.jpg'
try:
    import Image
except ImportError:
    from PIL import Image
from subprocess import check_output

# check_output(['convert', path, '-resample', '600', path])
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
captcha_output = pytesseract.image_to_string(Image.open(path))
print(captcha_output)
# input_captcha_text(captcha_output)

# if os.path.exists('captcha.jpg'):
#     os.remove('captcha.jpg')
# else:
#     print("The file does not exist")