# love sana twice
import os
import sys
import cv2

# add get module
from keras.preprocessing.image import load_img, save_img, img_to_array, array_to_img

target_size = [112,224]
images_dir = 'sign/taisei.bmp'  # input directory
image_save_dir = 'resize_image/'  # output directory
os.makedirs(image_save_dir,exist_ok=True
image_size = 224                    # ここはどうにか後で変えようかな？
if len(sys.argv) > 1:
    image_size = int(sys.argv[1])

def _main(dpi):
    im = cv2.imread('sign/taisei.bmp')  # <class 'numpy.ndarray'>
    print(im.shape)     # <tuple>
    aspect = im.shape[1] / im.shape[0]
    
    img = load_img(images_dir, grayscale=False, color_mode='rgb', target_size=(int(dpi),int(dpi*aspect)))
    i2ary = img_to_array(img)
    save_img(image_save_dir+ "{}.jpg".format(dpi), i2ary)
    a=0

    #resize_images_hry(images_dir=images_dir,image_save_dir=image_save_dir, image_size=image_size)


if __name__ == '__main__':
    for dpi in target_size:
        _main(dpi)