import cv2
import pytesseract
from PIL import Image


def unicodetoascii(text):
    uni2ascii = {
        ord('\xe2\x80\x99'): ord("'"),
        ord('\xe2\x80\x9c'): ord('"'),
        ord('\xe2\x80\x9d'): ord('"'),
        ord('\xe2\x80\x9e'): ord('"'),
        ord('\xe2\x80\x9f'): ord('"'),
        ord('\xc3\xa9'): ord('e'),
        ord('\xe2\x80\x9c'): ord('"'),
        ord('\xe2\x80\x93'): ord('-'),
        ord('\xe2\x80\x92'): ord('-'),
        ord('\xe2\x80\x94'): ord('-'),
        ord('\xe2\x80\x94'): ord('-'),
        ord('\xe2\x80\x98'): ord("'"),
        ord('\xe2\x80\x9b'): ord("'"),

        ord('\xe2\x80\x90'): ord('-'),
        ord('\xe2\x80\x91'): ord('-'),

        ord('\xe2\x80\xb2'): ord("'"),
        ord('\xe2\x80\xb3'): ord("'"),
        ord('\xe2\x80\xb4'): ord("'"),
        ord('\xe2\x80\xb5'): ord("'"),
        ord('\xe2\x80\xb6'): ord("'"),
        ord('\xe2\x80\xb7'): ord("'"),

        ord('\xe2\x81\xba'): ord("+"),
        ord('\xe2\x81\xbb'): ord("-"),
        ord('\xe2\x81\xbc'): ord("="),
        ord('\xe2\x81\xbd'): ord("("),
        ord('\xe2\x81\xbe'): ord(")"),

    }
    return text.translate(uni2ascii).encode('ascii')


def getTextFromImage(image):
    # save image to tmp directory
    try:
        cv2.imwrite("tmp/ocr.png", image)

        imageOcr = Image.open("tmp/ocr.png")
        text = pytesseract.image_to_string(imageOcr)
        return text
    except Exception as e:
        print(e)
