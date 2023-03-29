from Crypto.Cipher import AES
import os


def encriptar(key, path, name):
    chunk = 64 * 1024  # métrica usada para eer el archivo en bloques de 64 kilobytes
    extension = path[:-4]+'.aes'
    archivo_tamaño = str(os.path.getsize(path)).zfill(16)
    print(archivo_tamaño, extension)
