#Import the files
import qrcode
#Get the link from the user
qr_link = input("Please enter the link: ")
#Ask for the name of the image to save
qr_image_name = input("What is the name you would like to save the image with: ")
#Set the photo format with the value
qr_image_name = "%s.png"%qr_image_name
#Generate the qr image
qr_code = qrcode.make(qr_link)
#Save the qr image
qr_code.save(qr_image_name,"PNG")