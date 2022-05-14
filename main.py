from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

for k in os.listdir('.'):
    if k.endswith('.jpg') or k.endswith('.png'):
        img = Image.open(k)
        rgb_img = img.convert('RGB')
        fn, flext = os.path.splitext(k)

        # Resize
        img_res = rgb_img.resize((1080, 1080))
        width, height = img_res.size

        # Black and white
        img_res = img_res.convert('L')

        #Watermark
        draw = ImageDraw.Draw(img_res)
        text = "Sula69"
        txt_color = "purple"
        font = ImageFont.truetype("KZ_Century_Gothic.ttf", 180)
        textwidth, textheight = draw.textsize(text, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, txt_color, font=font)

        img_res.save('Result/{}{}'.format(fn, flext))
