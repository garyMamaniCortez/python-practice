import cv2
# read image
image=cv2.imread('contorno.jpg')
# convert image to gray
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# umbral
tipoUmbral,umbral=cv2.threshold(gray,30,255,cv2.THRESH_BINARY)
#contours
outline,hierarchy = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image,outline,-1,(65,105,225),2)
# show image
cv2.imshow('gray',gray)
cv2.imshow('umbral',umbral)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
