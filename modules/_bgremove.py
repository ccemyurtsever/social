from rembg import remove
from PIL import Image

input_path = 'xxx.jpg'
output_path = 'xxxxxx.png'

print("Before opening image")
input_image = Image.open(input_path)

print("Before removing background")
output_image = remove(input_image)

print("Before saving output")
output_image.save(output_path)

print("Process completed")
