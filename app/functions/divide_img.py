import cv2
import numpy as np


def function(path, name):
    carpeta_img = path
    open_img = name
    img = cv2.imread(carpeta_img, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cb, cr = cv2.split(img_yuv)
    ycb = cv2.merge([y, cb, np.zeros_like(cb)])
    cv2.imwrite(carpeta_img[:-4]+'-YCb-'+open_img[-4:], ycb)
    string = f'{carpeta_img[:-4]}-YCb-{open_img[-4:]}'
    return string
