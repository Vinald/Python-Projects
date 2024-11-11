import time
import pyotp

key = pyotp.random_base32()
print("Key: ", key)

# key = 'okirorsamuelvinald'

totp = pyotp.TOTP(key)
print("Current OTP: ", totp.now())

# time.sleep(30)
# print("Current OTP: ", totp.now())

input_otp = input("Enter OTP: ")
if totp.verify(input_otp):
    print("OTP Verified")
    

