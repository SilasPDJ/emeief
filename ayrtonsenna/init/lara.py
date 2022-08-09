import sys
from PIL import Image
import os
PATH = r"C:\Users\sbferreira\OneDrive\BKP SECRETARIA\SILAS\LARA\2cicloB"

images = os.listdir(PATH)
images = [os.path.join(PATH, arq) for arq in images if arq.endswith(
    ".png") or arq.endswith(".jpg")]
# images = sys.argv[1:]

# eval,s
# exec()
ima = None
imalist = []
for im in images:
    im_image = Image.open(im)
    im_rgb = im_image.convert('RGB')
    imalist.append(im_rgb)
imalist.pop()

im_rgb.save(r'my_images_pt3.pdf',
            save_all=True, append_images=imalist)
