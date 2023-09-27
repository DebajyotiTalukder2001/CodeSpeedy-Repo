

# Decoding

# pip install opencv-python

import cv2   

# Open the desired image (can also be a jpg)
img = cv2.imread("img/qr_App.png")
# Instantiate a new detector object
detector = cv2.QRCodeDetector()
# Decode the image
data = detector.detectAndDecode(img)
# Show the results
print("Output from QRCode:")
print(data[0])

