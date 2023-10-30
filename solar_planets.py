import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "sol", (100,80),cv2.FONT_HERSHEY_COMPLEX,2, (0,0,255))
cv2.putText(img, "mercurio", (110,250),cv2.FONT_HERSHEY_COMPLEX,0.5, (0,0,255))
cv2.putText(img, "venus", (195,250),cv2.FONT_HERSHEY_COMPLEX,0.5, (0,0,255))
cv2.putText(img, "terra", (290,260),cv2.FONT_HERSHEY_COMPLEX,0.5, (0,0,255))








cv2.imshow("results", img)

cv2.waitKey(0)

