import image
import qrcode
qr = qrcode.QRCode(
    version = 7,
    box_size= 4,
    border= 4
)
 
link = "https://www.youtube.com/watch?v=T3xf42BvUak"

qr.add_data(link)
qr.make(fit= True)
img = qr.make_image(fill = "Black", back_color = "White")
img.save("MR BEAN.png")