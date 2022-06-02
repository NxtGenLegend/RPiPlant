import cv2

port = 0
cam = cv2.videocapture(port)
img = cam.read()
cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0) 
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1) 
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1) 

cv2.imshow("X", sobelx)
cv2.waitKey(0)
cv2.imshow("Y", sobely)
cv2.waitKey(0)
cv2.imshow("X & Y", sobelxy)
cv2.waitKey(0)

edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

cv2.imshow("Edges", edges)
cv2.waitKey(0)

cv2.destroyAllWindows()
