import cv2
import numpy as np
from fastapi.responses import JSONResponse


def function(path, name):
    carpeta_img = path
    open_img = name
    img = cv2.imread(carpeta_img, cv2.IMREAD_COLOR)
    size = (640, 480)
    img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cb, cr = cv2.split(img_yuv)
    ycb = cv2.merge([y, cb, np.zeros_like(cb)])
    ycr = cv2.merge([y, np.zeros_like(cr), cr])
    cv2.imwrite(carpeta_img[:-4]+'-Y-'+open_img[-4:], y)
    cv2.imwrite(carpeta_img[:-4]+'-Cb-'+open_img[-4:], cb)
    cv2.imwrite(carpeta_img[:-4]+'-Cr-'+open_img[-4:], cr)
    cv2.imwrite(carpeta_img[:-4]+'-YCb-'+open_img[-4:], ycb)
    cv2.imwrite(carpeta_img[:-4]+'-YCr-'+open_img[-4:], ycr)
    img_y = f'{carpeta_img[:-4]}-Y-{open_img[-4:]}'
    img_cb = f'{carpeta_img[:-4]}-Cb-{open_img[-4:]}'
    img_cr = f'{carpeta_img[:-4]}-Cr-{open_img[-4:]}'
    return {
        "img_yfile": img_y,
        "img_cbfile": img_cb,
        "img_crfile": img_cr,
        "size": size
    }
