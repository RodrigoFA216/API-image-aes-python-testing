from fastapi import APIRouter, UploadFile, File
import shutil
from typing import List
from fastapi.responses import JSONResponse, FileResponse

from app.schemas.item_scheme import ItemScheme

router = APIRouter()

# Carpetas de archivos
imgFolder = 'app/temp/img/'
imgCifFolder = 'app/temp/imgCif/'

# Formatos válidos
imgFormats = ('.png', '.jpg', 'jpeg', '.bmp')


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


@router.post('/API/Encrypt/Image/Multiple', tags=['Post', 'Recive Multiple Imagen', 'encrypt'])
async def uploadImg(files: List[UploadFile] = File(...)):
    try:
        for img in files:
            with open(f'{img.filename}', 'wb') as F:
                shutil.copyfileobj(img.file, F)
        return JSONResponse(content={"file_name": "Good"}, status_code=200)
    except:
        return JSONResponse(content={"Error": "Algo falló con el archivo"}, status_code=205)


@router.post('/API/Encrypt/Image/V2', tags=['Post', 'Recive Imagen', 'encrypt'])
async def reciveImage(file: UploadFile = File(...)):
    try:
        if file.filename[-4:] in imgFormats:
            with open(f'{imgFolder}{file.filename}', 'wb') as F:
                shutil.copyfileobj(file.file, F)
            path = f'{imgFolder}{file.filename}'
            return FileResponse(path)
        else:
            return JSONResponse(content={"Error": "La extención del archivo no es válida"}, status_code=200)
    except:
        return JSONResponse(content={"Error": "Algo falló con el archivo"}, status_code=205)
