from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from typing import List
import os
from os import getcwd
import shutil
from dotenv import load_dotenv

from app.schemas.item_scheme import ItemScheme
from app.functions import divide_img, AES_cypher

router = APIRouter()

# Carpetas de archivos
imgFolder = 'app/temp/img/'
imgCifFolder = 'app/temp/imgCif/'

# Formatos válidos
imgFormats = ('.png', '.jpg', '.bmp')

# crear las instancias del objeto AES
clave = b'LlaveSecreta1234'  # la clave debe tener 16, 24 o 32 bytes de longitud
iv = b'VectorInicial123'  # el vector inicial debe tener 16 bytes de longitud


@router.post('/API/Encrypt/Image/V3', tags=['Post', 'Recive Imagen', 'encrypt'])
async def reciveImage(file: UploadFile = File(...)):
    if file.filename[-4:] in imgFormats:
        # Uno la ruta de imgFolder con el nombre del archivo menos la extensión
        file_folder = os.path.join(imgFolder, file.filename[:-4])
        # Creo la ruta final del archivo
        os.makedirs(file_folder, exist_ok=True)
        # Guardo el archivo dentro de la carpeta
        file_path = os.path.join(file_folder, file.filename)
        with open(file_path, 'wb') as F:
            content = await file.read()
            F.write(content)
            F.close()
        response = divide_img.function(file_path, file.filename)
        AES_cypher.cypher_image(clave, iv, file_path, file.filename)
        # rmtree(file_folder)
        print(file_path)
        return FileResponse(response['img_yfile'])
    else:
        return JSONResponse(content={"Error": "La extención del archivo no es válida"}, status_code=200)


@router.post('/API/Encrypt/Image', tags=['Post', 'Recive Imagen', 'encrypt'])
async def reciveImage(file: UploadFile = File(...)):
    try:
        if file.filename[-4:] in imgFormats:
            with open(f'{imgFolder}{file.filename}', 'wb') as F:
                shutil.copyfileobj(file.file, F)
            return JSONResponse(content={"file_name": file.filename}, status_code=200)
        else:
            return JSONResponse(content={"Error": "La extención del archivo no es válida"}, status_code=200)
    except:
        return JSONResponse(content={"Error": "Algo falló con el archivo"}, status_code=205)


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
