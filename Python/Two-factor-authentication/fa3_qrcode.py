import qrcode
import pyotp

key = 'okirorsamuelvinald'

uri = pyotp.totp.TOTP(key).provisioning_uri(name='okiror samuel vinald', issuer_name='2FA using python')

print(uri)

qrcode.make(uri).save('qrcode.png') 

totp = pyotp.TOTP(key)

input_otp = input("Enter OTP: ")
if totp.verify(input_otp):
    print("OTP Verified")
