

import os
import qrcode

webpage = input("webpage: ")

img = qrcode.make(f" Webpage: {webpage}")
img.save("qr.png", "PNG")

