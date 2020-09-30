#!/usr/bin/python3

from PIL import Image

img_path=input("Enter the path of image : ")
image1 = Image.open(img_path)

im1 = image1.convert('RGB')

pdf_path=input("Enter the name of New PDF file : ")
im1.save(f"{pdf.path}.pdf")
