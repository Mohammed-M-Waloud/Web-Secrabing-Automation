import cv2
import pytesseract

tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("ugfqpdxzxthh.png")
img = cv2.resize(img, None, fx=2, fy=2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 20)
print((pytesseract.image_to_string(img, config=tessdata_dir_config)).strip())
print((pytesseract.image_to_string(gray, config=tessdata_dir_config)).strip())
print((pytesseract.image_to_string(adaptive, config=tessdata_dir_config)).strip())

cv2.imshow("Captcha", img) # Output: IMQW
cv2.imshow("Gray", gray) # Output: IMOW
cv2.imshow("Adaptive", adaptive) # Output: IMOW,

cv2.waitKey(7000)