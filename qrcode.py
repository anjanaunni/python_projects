import pyqrcode
import png
from pyqrcode import QRCode
QRstring="paste your url here"
url=pyqrcode.create(QRstring)
url.png('qr.png',scale=8)
