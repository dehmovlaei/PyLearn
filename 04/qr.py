import qrcode
name = input("enter your name:\n")
phone = input("enter your phone number:\n")
qrString = name + " | Phone Number: " + phone
qr = qrcode.make(qrString)
qr.save("myQr.png")
print("done")

