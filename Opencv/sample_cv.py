import cv2


img=cv2.imread('leena.jpg',1)
cv2.imshow('output image',img)
print(img)
cv2.waitKey(0)

cv2.destroyAllWindows()