from fastapi import APIRouter, UploadFile, File
import shutil
from typing import List

from app.schemas.item_scheme import ItemScheme

router = APIRouter()

# Carpetas de archivos
imgFolder = 'app/temp/img/'
imgCifFolder = 'app/temp/imgCif/'


@router.post('/API/Encrypt/Image', tags=['Post', 'Recive Imagen', 'encrypt'], status_code=200, response_description="Petición válida")
async def reciveImage(file: UploadFile = File(...)):
    with open(f'{imgFolder}{file.filename}', 'wb') as F:
        shutil.copyfileobj(file.file, F)
    return {"file_name": file.filename}


@router.post('/API/Encrypt/Image/Multiple', tags=['Post', 'Recive Imagen', 'encrypt'], status_code=200, response_description="Petición válida")
async def uploadImg(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', 'wb') as F:
            shutil.copyfileobj(img.file, F)
    return {"file_name": "Good"}
