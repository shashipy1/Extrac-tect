import pytesseract
from PIL import Image

pytesseract.pytesseract.tessract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open("acsp.png")
text = pytesseract.image_to_string(img)
print(text)