# love sana
import os
import sys

# add get module
import os , sys
from glob import glob
from PIL import Image

from keras.preprocessing.image import load_img, save_img, img_to_array, array_to_img


def resize_images(image_path, image_save_dir, image_size):
    img = load_img(image_path, grayscale=False, color_mode='rgb', target_size=(224,224))
    a=0




def _main():
    images_dir = 'sign/sana.png'  # input directory
    image_save_dir = 'resize_image/'  # output directory
    image_size = 100                    # ここはどうにか後で変えようかな？
    if len(sys.argv) > 1:
        image_size = int(sys.argv[1])

    resize_images(images_dir=images_dir, image_save_dir=image_save_dir, image_size=image_size)


if __name__ == '__main__':
    _main()