import qrcode
from qrtools import QR

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)


def aepsimps():
    data = ["Name = XYZ", "Account Number = 58485615815588", "Phone no.= 8761656525", "Aadhar Number = 1258763265665442", "IFSC Code = YES10251520230"],

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save("aepsimps.png")
    return 1


def upineft():
    data = ["Name = XYZ", "UPI ID = AshishT11@oksbi", "Location Code = 06748","Name = XYZ", "Account Number = 2259761156215", "IFSC Code = KKBK0006562", "Branch Address = Masab Tank, Hyderabad"],

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save("upineft.png")
    return 1

def impsupi():
    data = ["Name = XYZ", "Account Number = 58485615815588", "Phone no.=8761656525","Name = XYZ", "UPI ID = AshishT11@oksbi", "Location Code = 06748"],

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save("impsupi.png")
    return 1


def aepsupi():
    data = ["Account Number=25761523148315", "Aadhaar number=2346784320","Name = XYZ", "UPI ID = AshishT11@oksbi", "Location Code = 06748"],

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save("aepsupi.png")
    return 1


def impsneft():
    data = ["Name = XYZ", "Account Number = 58485615815588", "Phone no.=8761656525","Name = XYZ", "Account Number = 2259761156215", "IFSC Code = KKBK0006562", "Branch Address = Masab Tank, Hyderabad"],

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save("impsneft.png") 									
    return 1


def aepsneft():
    data = ["Account Number=25761523148315", "Aadhaar number=2346784320","Name = XYZ", "Account Number = 2259761156215", "IFSC Code = KKBK0006562", "Branch Address = Masab Tank, Hyderabad"],

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save("aepsneft.png") 
    return 1

def numbers(argument):
    switcher = {
        1: impsaeps,
        2: upineft,
        3: impsupi,
        4: aepsupi,
        5: impsneft,
        6: aepsneft

    }


    func = switcher.get(argument, lambda: "Invalid Choice")
    print func()




















									
