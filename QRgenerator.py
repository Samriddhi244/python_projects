import qrcode as qr
provide_link = "i love you"
img = qr.make(provide_link)
img.save("saved")