import image
import qrcode
qr = qrcode.QRCode(
    version = 7,
    border= 5,
    box_size= 3

)

link = "https://www.youtube.com/watch?v=T3xf42BvUak"


qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill = "balck", back_color = "white")
img.save("Mr Bean 2.png")