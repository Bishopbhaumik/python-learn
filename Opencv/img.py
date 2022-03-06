from PIL import Image,ImageEnhance, ImageFilter
import os
img1=Image.open("leena.jpg")
# img1.save("leena1.png")
# # img1.show()
# max=(250,250)
# img1.thumbnail(max)
# img1.save("leena_sm.jpg")
# enh=ImageEnhance.Sharpness(img1)
# enh.enhance(1).save("test.jpg")
# enh=ImageEnhance.Color(img1)
# enh.enhance(1).save("test.jpg")

img1.filter(ImageFilter.GaussianBlur(radius=4)).save("test.jpg")