#!/usr/bin/python3

#Importing the required libraries
from os import path
from PIL import Image

def main():

    #Taking the path of image
    img_path=str(input("Enter the path of image : "))

    #Checking if the file exist or not
    if path.exists(img_path) != True:
        print("\nError, File dont exist")
        exit(0)
    else:    
        image=Image.open(img_path)
        img=image.convert('RGB')

        pdf_path=str(input("Enter the name of New PDF file : "))

        if pdf_path == "":
            print("\nError, Please Enter the PDF name.")
        else:
            img.save(f"{pdf_path}.pdf")

#Calling the main function
if __name__ == "__main__":
    main()