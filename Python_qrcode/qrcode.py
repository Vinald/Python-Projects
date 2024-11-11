import qrcode.qrcode as qrcode

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=10
)
data = "https://getbootstrap.com/docs/5.2/getting-started/introduction/"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('test.png')
