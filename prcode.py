import qrcode

img = qrcode.make("Hello world")
img.save("code.png")



















# import qrcode
# from qrcode.image.styledpil import StyledPilImage
# from qrcode.image.styles.colormasks import SolidFillColorMask
# # import pillow

# data = input("Enter qr code link/data: ")

# qr = qrcode.QRCode(
#     version=1,
#     box_size=10,
#     border=1
# )

# qr.add_data(data)
# qr.make(fit=True)

# img = qr.make_image(image_factory=StyledPilImage,
#                     color_mask = SolidFillColorMask(back_color="white", front_color="red"))

# img.save("colored_qr.png")