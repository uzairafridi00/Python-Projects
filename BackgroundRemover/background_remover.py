# pip install rembg
# pip install pillow
from rembg import remove
from PIL import Image
image_input = Image.open()
output = remove(image_input)
output.save('./test/result.png')
