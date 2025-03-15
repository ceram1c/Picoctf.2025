from PIL import Image
import stepic

img = Image.open("upz.png")

decoded_message = stepic.decode(img)

print(decoded_message)