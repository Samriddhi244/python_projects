import qrcode as qr
provide_link = input("enter the url")
img = qr.make(provide_link)
img.save("saved")