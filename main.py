# QR code creator 

import pyqrcode
import png
from pyqrcode import *


# String which the QR code will call to 
s = 'www.xyz.com'

# Generates the QR code
url = pyqrcode.create(s)

# Create and save the svg file 
url.svg('test.svg', scale = 15)

# Create and save the png file 
url.png('test.png', scale = 35) # a good size for filling up a page
