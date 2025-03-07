from PIL import Image


otahuku_img = Image.open("images/otahuku.png")
# otahuku_img.show()

print(otahuku_img.split())
otahuku_img.split()[0].show()
otahuku_img.split()[1].show()
otahuku_img.split()[2].show()
otahuku_img.split()[3].show()
