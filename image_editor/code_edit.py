
"""
Created on Tue Jul 14 10:24:15 2020

@author: Sivaraman Sivaraj
"""

from PIL import Image, ImageFilter


#creating a image object
im1 = Image.open("original.jpg")

#applying various filters
im2 = im1.filter(ImageFilter.BLUR)
im3 = im1.filter(ImageFilter.CONTOUR)
im4 = im1.filter(ImageFilter.EMBOSS)
im5 = im1.filter(ImageFilter.EDGE_ENHANCE)

# im2.show()
# im3.show()
# im4.show()
# im5.show()


