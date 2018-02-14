from PIL import Image
import cv2
import time

camera = cv2.VideoCapture(0)
time.sleep(0.2)
return_value, image = camera.read()
cv2im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pilim = Image.fromarray(cv2im)
del camera
bmp = pilim.convert('L').resize([60, 60])
bmp.save("Check\phand.jpg")
