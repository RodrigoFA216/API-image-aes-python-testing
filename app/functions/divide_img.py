import cv2
import numpy as np
from fastapi.responses import JSONResponse
import os
from scipy.ndimage import zoom


def divide(path, name):
    carpeta_img = path
    open_img = name
    img = cv2.imread(carpeta_img, cv2.IMREAD_COLOR)
    height, width, channels = img.shape
    resize_height = height//2
    resize_width = width//2
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cb, cr = cv2.split(img_yuv)
    ycb = cv2.merge([y, cb, np.zeros_like(cb)])
    ycr = cv2.merge([y, np.zeros_like(cr), cr])
    cv2.imwrite(carpeta_img[:-4]+'-Y-'+open_img[-4:], y)
    cv2.imwrite(carpeta_img[:-4]+'-Cb-'+open_img[-4:], cb)
    cv2.imwrite(carpeta_img[:-4]+'-Cr-'+open_img[-4:], cr)
    cv2.imwrite(carpeta_img[:-4]+'-YCb-'+open_img[-4:], ycb)
    cv2.imwrite(carpeta_img[:-4]+'-YCr-'+open_img[-4:], ycr)
    # ---------------------------Reducir componentes--------------------------------
    # Reducir la componente Cb
    cb_redux = cv2.resize(cb, (resize_width, resize_height),
                          interpolation=cv2.INTER_CUBIC)
    # Aplicar antialiasing
    cb_redux_smooth = cv2.GaussianBlur(cb_redux, (3, 3), 0)
    # Reducir la componente Cr
    cr_redux = cv2.resize(cr, (resize_width, resize_height),
                          interpolation=cv2.INTER_CUBIC)
    # Aplicar antialiasing
    cr_redux_smooth = cv2.GaussianBlur(cr_redux, (3, 3), 0)
    # Guardar las imagenes resultantes
    cv2.imwrite(carpeta_img[:-4]+"-cb-min-"+open_img[-4:], cb_redux_smooth)
    cv2.imwrite(carpeta_img[:-4]+"-cr-min-"+open_img[-4:], cr_redux_smooth)
    img_y = f'{carpeta_img[:-4]}-Y-{open_img[-4:]}'
    cb_resize_path = f'{carpeta_img[:-4]}-cb-min-{open_img[-4:]}'
    cr_resize_path = f'{carpeta_img[:-4]}-cr-min-{open_img[-4:]}'
    return {
        "img_crfile": cr_resize_path,
        "img_cbfile": cb_resize_path,
        "or_h": height,
        "or_w": width,
        "resize_h": resize_height,
        "resize_w": resize_width,
        "img_yfile": img_y
    }


def merge(path_cb, path_cr, path_y, res_h, res_w, name):
    or_h = res_h*2
    or_w = res_w*2
    open_img = name
    y = cv2.imread(path_y, cv2.IMREAD_COLOR)
    cb = cv2.imread(path_cb, cv2.IMREAD_COLOR)
    cr = cv2.imread(path_cr, cv2.IMREAD_COLOR)
    # Redimensionar las componentes de color
    cb_redim = cv2.resize(cb, (or_w, or_h),
                          interpolation=cv2.INTER_CUBIC)
    cr_redim = cv2.resize(cr, (or_w, or_h),
                          interpolation=cv2.INTER_CUBIC)
    # Aplicar GaussianBlur
    cb_redim_smooth = cv2.GaussianBlur(cb_redim, (3, 3), 0)
    cr_redim_smooth = cv2.GaussianBlur(cr_redim, (3, 3), 0)
    merged_smooth = cv2.merge([y, cb_redim, cr_redim])
    cv2.imwrite(carpeta_save[:-1]+"\Merged-smooth.bmp", merged_smooth)


# def function(path, name):
#     carpeta_img = path
#     open_img = name
#     img = cv2.imread(carpeta_img, cv2.IMREAD_COLOR)
#     size = (640, 480)
#     img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
#     img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
#     y, cb, cr = cv2.split(img_yuv)
#     ycb = cv2.merge([y, cb, np.zeros_like(cb)])
#     ycr = cv2.merge([y, np.zeros_like(cr), cr])
#     cv2.imwrite(carpeta_img[:-4]+'-Y-'+open_img[-4:], y)
#     cv2.imwrite(carpeta_img[:-4]+'-Cb-'+open_img[-4:], cb)
#     cv2.imwrite(carpeta_img[:-4]+'-Cr-'+open_img[-4:], cr)
#     cv2.imwrite(carpeta_img[:-4]+'-YCb-'+open_img[-4:], ycb)
#     cv2.imwrite(carpeta_img[:-4]+'-YCr-'+open_img[-4:], ycr)
#     img_y = f'{carpeta_img[:-4]}-Y-{open_img[-4:]}'
#     img_cb = f'{carpeta_img[:-4]}-Cb-{open_img[-4:]}'
#     img_cr = f'{carpeta_img[:-4]}-Cr-{open_img[-4:]}'
#     return {
#         "img_yfile": img_y,
#         "img_cbfile": img_cb,
#         "img_crfile": img_cr,
#         "size": size
#     }


def reduce_components(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    height, width, channels = img.shape
    resize_height = height//2
    resize_width = width//2
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cb, cr = cv2.split(img_yuv)

    # Reducir la componente Cb
    cb_redux = cv2.resize(cb, (resize_width, resize_height),
                          interpolation=cv2.INTER_CUBIC)
    # Aplicar antialiasing
    cb_redux_smooth = cv2.GaussianBlur(cb_redux, (3, 3), 0)

    # Reducir la componente Cr
    cr_redux = cv2.resize(cr, (resize_width, resize_height),
                          interpolation=cv2.INTER_CUBIC)
    # Aplicar antialiasing
    cr_redux_smooth = cv2.GaussianBlur(cr_redux, (3, 3), 0)

    # Guardar las imagenes resultantes
    carpeta_save = os.path.dirname(image_path) + "/ImgYCbCr/"
    cv2.imwrite(carpeta_save + "componente-cb-min-blur.bmp", cb_redux_smooth)
    cv2.imwrite(carpeta_save + "componente-cr-min-blur.bmp", cr_redux_smooth)

    return carpeta_save + "componente-cb-min-blur.bmp", carpeta_save + "componente-cr-min-blur.bmp"
