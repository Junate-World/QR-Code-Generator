import qrcode

def generate_qr_code(text, filename):
  qr = qrcode.QRCode(version=1, 
                     error_correction=qrcode.constants.ERROR_CORRECT_L, 
                     box_size=10, 
                     border=4)
  qr.add_data(text)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  img.save(filename)

filename = input("Enter filename and add .png extension: ")
text = input("Enter the data/text to encode in the QR code: ")

generate_qr_code(text, filename)

print(f"QR code generated successfully! as {filename}")