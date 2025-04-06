import pyqrcode
import png 
from pyqrcode import QRCode

print(" Welcome to Scanner generator!\n")
choose =int(input("""
        Choose the option below.
        1) Phone Number.
        2) Generate from link.
        """))

if choose==1:
    name =input("Name your scanner:")
    number = input("Enter the phone number (with country code, e.g., +91...): ")

    tel_link = f"tel:{number}"

    qr = pyqrcode.create(tel_link)


    qr.png(f"{name}.png", scale=8)

    print(f"QR code saved as '{name}'. Scan it with your phone camera to call the number!")

elif choose==2:
    name =input("Name your scanner:")
    s = input("Enter the link or text to encode in QR code: ")

    url = pyqrcode.create(s)

    url.svg(f"{name}.svg", scale=8)
    url.png(f"{name}.png", scale=8)

    print("QR code has been saved as 'myqr.svg' and 'myqr.png'")

else: 
    print("invalid option")
