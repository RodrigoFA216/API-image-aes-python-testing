import cv2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# cargar la imagen
img = cv2.imread('app/temp/img/Atmosfera/Atmosfera-Y-.jpg',
                 cv2.IMREAD_GRAYSCALE)

# crear una instancia del objeto AES
clave = b'LlaveSecreta1234'  # la clave debe tener 16, 24 o 32 bytes de longitud
iv = b'VectorInicial123'  # el vector inicial debe tener 16 bytes de longitud
aes = AES.new(clave, AES.MODE_OFB, iv)

# aplicar el cifrado
img_cifrada = aes.encrypt(pad(img.tobytes(), AES.block_size))

# guardar la imagen cifrada
with open('app/temp/img/Atmosfera/Atmosfera-cif-.enc', 'wb') as f:
    f.write(img_cifrada)


def cypher_image(key, vector, path, name):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    aes = AES.new(key, AES.MODE_OFB, vector)
    # Aplicar el cifrado
    img_cifrada = aes.encrypt(pad(img.tobytes(), AES.block_size))
    with open(path[:last_slash_index+1]+name[:-4]+'-cif'+name[-4:], 'wb') as f:
        f.write(img_cifrada)
