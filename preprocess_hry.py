# love sana twice
# @ HRY CONSULTING
import os
import sys
import cv2

# add get module
from keras.preprocessing.image import load_img, save_img, img_to_array, array_to_img

target_size = [112,224,248,1404]
images_dir = 'sign/taisei.bmp'  # input directory
image_save_dir = 'resize_image/'  # output directory
os.makedirs(image_save_dir,exist_ok=True)

if len(sys.argv) > 1:
    image_size = int(sys.argv[1])

def _main(dpi):
    im = cv2.imread('sign/taisei.bmp')  # <class 'numpy.ndarray'>
    #print(im.shape)     # <tuple>
    assert dpi < im.shape[0] , "you choice too big dpi for comparing original pic size (%d->%d)"%(dpi , im.shape[0])
    aspect = im.shape[1] / im.shape[0]
    img = load_img(images_dir, grayscale=False, color_mode='rgb', target_size=(int(dpi),int(dpi*aspect)))
    i2ary = img_to_array(img)
    save_img(image_save_dir+ "{}.bmp".format(dpi), i2ary)

if __name__ == '__main__':
    for dpi in target_size:
        _main(dpi)