from pdf2docx import Converter

pdf_file = input("Dönüştürülecek Pdf Dosyasının Adını Giriniz")

docx_file = "word.docx"


cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()