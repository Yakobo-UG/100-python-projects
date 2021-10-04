import image
import qrcode
qr = qrcode.QRCode(
    version = 7,
    border= 4,
    box_size= 4
)

link = "https://www.youtube.com/watch?v=T3xf42BvUak"

qr.add_data(link)
qr.make(fit= True)
img = qr.make_image(back_color = "White", fill = "white")
img.save("Mr Bean.jpeg")