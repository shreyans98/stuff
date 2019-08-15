import qrcode
from qrtools import QR

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

data = ["Name = XYZ", "Account Number = 58485615815588", "Phone no.=8761656525", "IFSC Code = KKBK0006562", "Branch Address = Masab Tank, Hyderabad"],

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()
img.save("impsneft.png")
