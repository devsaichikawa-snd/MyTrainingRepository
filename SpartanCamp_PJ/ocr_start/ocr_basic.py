from PIL import Image
import pyocr


# オブジェクトの生成
tools = pyocr.get_available_tools()
# tesseractを格納
tool = tools[0]
# print(tool.get_name())

img = Image.open("camp_logo_english.png")
# img.show()
txt = tool.image_to_string(img, lang="eng+jpn", builder=pyocr.builders.TextBuilder())

print(txt)
