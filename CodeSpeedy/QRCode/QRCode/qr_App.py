
# pip install qrcode
# pip install Pillow

# importing the qrcode module 
import qrcode  
from PIL import Image
# creating a QRCode object  
qr = qrcode.QRCode(  
    version = 2,  
    error_correction = qrcode.constants.ERROR_CORRECT_L,  
    box_size = 20,  
    border = 5,  
)  
# using the add_data() function  
print("Enter any URL:")
qr.add_data(input())  
# using the make() function  
qr.make(fit = True)  
# using the make_image() function  
qr_img = qr.make_image(fill_color = "black", back_color = "white")  
# saving the QR code image  
qr_img.save("img/qr_App.png") 

print("Successfully Generated QR Code.")
#read the image

img = Image.open("img/qr_App.png")

#show image
img.show()


