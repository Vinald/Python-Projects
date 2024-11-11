import pyotp
import time

key = pyotp.random_base32()

counter = 0
htop = pyotp.HOTP(key)

for i in range(5):
    print("OTP: ", htop.at(counter))
    counter += 1
    time.sleep(2)
    
# verify OTP
input_otp = input("Enter OTP: ")
if htop.verify(input_otp, counter):
    print("OTP Verified")