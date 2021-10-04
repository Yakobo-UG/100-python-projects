import image
import qrcode
qr = qrcode.QRCode(
    version = 7,
    box_size= 5,
    border= 3
)

link = "https://www.youtube.com/watch?v=T3xf42BvUak"

qr.add_data(link)
qr.make(fit= True)
img = qr.make_image(fill = "white", back_color = "Black")
img.save("Mr Bean 3.png")
