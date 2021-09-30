from PIL import Image
import numpy as np

im = Image.open('schecter.png')
def sepia(pixel):
    if pixel[0] < 100:
        r,g,b = int(pixel[0]*1.1), pixel[1], int(pixel[2]*.9)
    elif pixel[0]>62 and pixel[0]<192:
        r,g,b = int(pixel[0]*1.15), pixel[1], int(pixel[2]*.85)
    else:
        r = int(pixel[0]*1.08)
        if r>=255: r=130
        g,b = pixel[1], pixel[2]//2  
    return r,g,b
sepia_list = map(sepia, im.getdata())
im.putdata(list(sepia_list))
im.show()

# ---------------------------------------------------------------------

# def copy_image(your_image):
#     img = Image.open(your_image)
#     w,h = img.width, img.height
#     canvas = Image.new('RGB', (w,h), 'lime')
#     # canvas = Image.new('RGB', ((w//2)+1,(h//2)+1), 'lime')

#     target_x = 0
#     for source_x in range(0, img.width, 2):
#         target_y = 0
#         for source_y in range(0, img.height, 2):
#             pixel = img.getpixel((source_x, source_y))
#             canvas.putpixel((target_x, target_y), pixel)
#             target_y += 1
#         target_x += 1
#     canvas.show()

# copy_image('schecter.png')

# ---------------------------------------------------------------------

# def border_maker(your_image, border, color):
#     src = Image.open(your_image)
#     w,h = src.width, src.height
#     new_w, new_h = w+(2*border),h+(2*border)
#     trg = Image.new('RGB', (new_w, new_h), color)
#     for trg_x, src_x in enumerate(range(w), border):
#         for trg_y, src_y in enumerate(range(h), border):
#             px = src.getpixel((src_x, src_y))
#             trg.putpixel((trg_x, trg_y), px)
#     trg.show()

# border_maker('schecter.png', 5, 'yellow')

# ---------------------------------------------------------------------

# def shrinker(your_image, shrink_factor):
#     src = Image.open(your_image)
#     w,h = src.width, src.height
#     trg = Image.new('RGB', ((w//shrink_factor)+1,(h//shrink_factor)+1))
#     # trg = Image.new('RGB', (w,h))
#     for trg_x, src_x in enumerate(range(0, w, shrink_factor)):
#         for trg_y, src_y in enumerate(range(0, h, shrink_factor)):
#             px = src.getpixel((src_x, src_y))
#             trg.putpixel((trg_x, trg_y), px)
#     trg.show()

# shrinker('schecter.png', 4)

# ---------------------------------------------------------------------

# def scaler(your_image, mf):
#     source = Image.open(your_image)
#     w, h = source.width*mf,source.height*mf
#     target = Image.new('RGB', (w, h))
#     for target_x, source_x in enumerate(np.repeat(range(source.width), mf)):
#         for target_y, source_y in enumerate(np.repeat(range(source.height), mf)):
#             pixel = source.getpixel((int(source_x), int(source_y)))
#             target.putpixel((target_x, target_y), pixel)
#     target.show()

# scaler('schecter.png', 2)

# ---------------------------------------------------------------------

# source = Image.open('jeanne_small.jpg')
# target = Image.open('beach_old.jpg')

# w,h = source.width, source.height

# x_shift = 240
# y_shift = 1300

# for src_x, trg_x in enumerate(range(x_shift, w+x_shift)):
#   for src_y, trg_y in enumerate(range(y_shift, h+y_shift)):
#     r_s, g_s, b_s = source.getpixel((src_x, src_y))
#     r_t, g_t, b_t = target.getpixel((trg_x, trg_y))
#     blend = ( (r_s+r_t)//2, (g_s+g_t//2), (b_s+b_t)//2 )
#     target.putpixel((trg_x, trg_y), blend)

# target.show()