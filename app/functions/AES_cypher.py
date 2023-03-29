from Crypto.Cipher import AES
import os


def encriptar(key, path, name):
    llave = b'0123456789abcdef01234567'
    chunk = 64 * 1024  # métrica usada para eer el archivo en bloques de 64 kilobytes
    chunk = int(chunk)
    extension = path[:-4]+'.aes'
    archivo_tamaño = str(os.path.getsize(path)).zfill(16)
    IV = os.urandom(16)
    encryptor = AES.new(llave, AES.MODE_OFB, IV)
    with open(path, 'rb') as infile:
        with open(extension, 'wb') as outfile:
            outfile.write(archivo_tamaño.encode('utf-8'))
            outfile.write(IV)
            while True:
                chunk = infile.read(int(chunk))
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))
                outfile.write(encryptor.encrypt(chunk))
