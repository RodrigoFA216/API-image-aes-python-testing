from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from typing import List
import os
from os import getcwd
import shutil
from dotenv import load_dotenv

from app.schemas.item_scheme import ItemScheme
from app.functions import divide_img, AES_cypher, AES_decrypt
from app.functions.AES_cypher import cypher_image
from app.functions.AES_decrypt import decipher_image

router = APIRouter()

# Carpetas de archivos
imgFolder = 'app/temp/img/'
imgCifFolder = 'app/temp/imgCif/'

# Formatos válidos
imgFormats = ('.png', '.jpg', '.bmp')
cifFormats = ('.png', '.jpg', '.bmp', '.cif', '.aes')

# crear las instancias del objeto AES
clave = b'LlaveSecreta1234'  # la clave debe tener 16, 24 o 32 bytes de longitud
iv = b'VectorInicial123'  # el vector inicial debe tener 16 bytes de longitud


@router.post('/API/Encrypt/Image', tags=['Post', 'Recive Imagen', 'encrypt'])
async def reciveImage(file: UploadFile = File(...)):
    if file.filename[-4:] in imgFormats:
        # Uno la ruta de imgFolder con el nombre del archivo menos la extensión
        file_folder = os.path.join(imgFolder, file.filename[:-4])
        # Creo la ruta final del archivo
        os.makedirs(file_folder, exist_ok=True)
        # Guardo el archivo dentro de la carpeta
        file_path = os.path.join(file_folder, file.filename)
        print(file_path)
        with open(file_path, 'wb') as F:
            content = await file.read()
            F.write(content)
            F.close()
        # res_divide = divide_img.function(file_path, file.filename)
        res_divide = divide_img.divide(file_path, file.filename)
        res_cif = await cypher_image(clave, iv, file_path, file.filename)
        try:
            res_uncif = await decipher_image(clave, iv, file_path, file.filename)
        except:
            print("error en el descifrado")
        # rmtree(file_folder)
        # print(file_path)
        return FileResponse(res_cif)
    else:
        return JSONResponse(content={
            "Error": "La extención del archivo no es válida"
        }, status_code=200)
    # try:
    #     ...
    # except:
    #     return JSONResponse(content={
    #             "Error": "Algo falló con el archivo"
    #         }, status_code=205)


@router.post('/API/Encrypt/Image/Show', tags=['Post', 'Recive Imagen', 'encrypt'])
async def reciveImage(file: UploadFile = File(...)):
    if file.filename[-4:] in imgFormats:
        # Uno la ruta de imgFolder con el nombre del archivo menos la extensión
        file_folder = os.path.join(imgFolder, file.filename[:-4])
        # Creo la ruta final del archivo
        os.makedirs(file_folder, exist_ok=True)
        # Guardo el archivo dentro de la carpeta
        file_path = os.path.join(file_folder, file.filename)
        print(file_path)
        with open(file_path, 'wb') as F:
            content = await file.read()
            F.write(content)
            F.close()
        # res_divide = divide_img.function(file_path, file.filename)
        res_divide = divide_img.divide(file_path, file.filename)
        res_cif = AES_cypher.cypher_image(clave, iv, file_path, file.filename)
        # rmtree(file_folder)
        # print(file_path)
        return FileResponse(res_divide['img_yfile'])
    else:
        return JSONResponse(content={
            "Error": "La extención del archivo no es válida"
        }, status_code=200)
    # try:
    #     ...
    # except:
    #     return JSONResponse(content={
    #             "Error": "Algo falló con el archivo"
    #         }, status_code=205)


@router.post('/API/Decrypt/Image', tags=['Post', 'Recive Imagen', 'decrypt'])
async def reciveImage(file: UploadFile = File(...)):
    if file.filename[-4:] in cifFormats:
        file_folder = os.path.join(imgCifFolder, file.filename[:-4])
        os.makedirs(file_folder, exist_ok=True)
        file_path = os.path.join(file_folder, file.filename)
        print(file_path)
        with open(file_path, 'wb') as F:
            content = await file.read()
            F.write(content)
            F.close()
        AES_decrypt.decrypt_image(clave, iv, file_path, file.filename)
        return FileResponse(file_path)
    else:
        return JSONResponse(content={
            "Error": "La extención del archivo no es válida"
        }, status_code=200)
    # try:
    #     ...
    # except:
    #     return JSONResponse(content={
    #             "Error": "Algo falló con el archivo"
    #         }, status_code=205)


# @router.post('/API/Encrypt/Image/Multiple', tags=['Post', 'Recive Multiple Imagen', 'encrypt'])
# async def uploadImg(files: List[UploadFile] = File(...)):
#     try:
#         for img in files:
#             with open(f'{img.filename}', 'wb') as F:
#                 shutil.copyfileobj(img.file, F)
#         return JSONResponse(content={"file_name": "Good"}, status_code=200)
#     except:
#         return JSONResponse(content={"Error": "Algo falló con el archivo"}, status_code=205)


# @router.post('/API/Encrypt/Image/V2', tags=['Post', 'Recive Imagen', 'encrypt'])
# async def reciveImage(file: UploadFile = File(...)):
#     try:
#         if file.filename[-4:] in imgFormats:
#             with open(f'{imgFolder}{file.filename}', 'wb') as F:
#                 shutil.copyfileobj(file.file, F)
#             path = f'{imgFolder}{file.filename}'
#             return FileResponse(path)
#         else:
#             return JSONResponse(content={"Error": "La extención del archivo no es válida"}, status_code=200)
#     except:
#         return JSONResponse(content={"Error": "Algo falló con el archivo"}, status_code=205)
