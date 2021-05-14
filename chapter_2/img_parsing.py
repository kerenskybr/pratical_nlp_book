from PIL import Image
# sudo apt install tesseract-ocr
# pip3 install pytessercat
from pytesseract import image_to_string

file_name = "img/img.png"
text = image_to_string(Image.open(file_name))
print(text)