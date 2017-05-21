# -*- coding: utf-8 -*-
#%%
import cv2
import scipy.misc
#import ipdb
import numpy as np
#%%
def crop_resize(image_path, resize_shape=(64,64)):
    image = cv2.imread(image_path)
    height, width, channel = image.shape

    if width == height:
        resized_image = cv2.resize(image, resize_shape)
    elif width > height:
        resized_image = cv2.resize(image, (int(width * float(resize_shape[0])/height), resize_shape[1]))
        cropping_length = int( (resized_image.shape[1] - resize_shape[0]) / 2)
        resized_image = resized_image[:,cropping_length:cropping_length+resize_shape[1]]
    else:
        resized_image = cv2.resize(image, (resize_shape[0], int(height * float(resize_shape[1])/width)))
        cropping_length = int( (resized_image.shape[0] - resize_shape[1]) / 2)
        resized_image = resized_image[cropping_length:cropping_length+resize_shape[0], :]

    return (resized_image - 127.5) / 127.5
    #return resized_image/127.5 - 1
#%%

def save_visualization(X, (nh, nw), save_path='./vis/sample.jpg'):
    h,w = X.shape[1], X.shape[2]
    img = np.zeros((h * nh, w * nw, 3))

    for n,x in enumerate(X):
        j = n / nw
        i = n % nw
        img[j*h:j*h+h, i*w:i*w+w, :] = x

    scipy.misc.imsave(save_path, img)

#%%