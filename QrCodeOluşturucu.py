import pyqrcode

url = input("Lütfen Urlnizi Giriniz")

Qr_Kod = pyqrcode.create(url)
Qr_Kod.svg("Yeni Qr Kodunuz.svg ",scale=5)