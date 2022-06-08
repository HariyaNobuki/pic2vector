# love sana twice
import os
import sys

# add get module
import os , sys
from keras.preprocessing.image import load_img, save_img, img_to_array, array_to_img


def _main():
    images_dir = 'sign/taisei.bmp'  # input directory
    image_save_dir = 'resize_image/'  # output directory
    image_size = 224                    # ここはどうにか後で変えようかな？
    if len(sys.argv) > 1:
        image_size = int(sys.argv[1])
    
    img = load_img(images_dir, grayscale=False, color_mode='rgb', target_size=(224,224))
    iomaray = img_to_array(img)
    #an_pic = array_to_img(iomaray, scale=True)
    save_img("nsana.jpg", iomaray)
    a=0

    #resize_images_hry(images_dir=images_dir,image_save_dir=image_save_dir, image_size=image_size)


if __name__ == '__main__':
    _main()