from PIL import Image
import glob, os
from time import sleep


for invideo in glob.glob("video\*"):
    os.system('ffmpeg -i ' + invideo +' -filter:v "crop=2:1080:960:1" -q:v 1 temp/images-%04d.jpeg')

print("frames extracted")
sleep(1)


im_sequence = glob.glob("temp\*.jpeg")
im_size = (len(im_sequence), 1080)
composite = Image.new("RGB", im_size)
pix_col = 0

for infile in im_sequence:
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im_center = 1920 / 2
    im_strip = im.crop( (0, 0, 1, 1080) )
    composite.paste(im_strip, (pix_col, 0))
    pix_col += 1
    im.close()
    os.remove(infile)
    print(file)

composite.save("unwrapped.jpeg", "JPEG")
    
    
print("done")
