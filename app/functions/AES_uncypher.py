import cv2
import numpy
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# cargar la imagen cifrada
with open('ruta/de/la/imagen_cifrada.enc', 'rb') as f:
    img_cifrada = f.read()

# crear una instancia del objeto AES
clave = b'LlaveSecreta1234'  # la clave debe tener 16, 24 o 32 bytes de longitud
iv = b'VectorInicial123'  # el vector inicial debe tener 16 bytes de longitud
aes = AES.new(clave, AES.MODE_OFB, iv)

# aplicar el descifrado
img_descifrada = unpad(aes.decrypt(img_cifrada), AES.block_size)

# convertir la imagen descifrada a su formato original
img_descifrada = cv2.imdecode(
    numpy.frombuffer(img_descifrada, numpy.uint8),
    cv2.IMREAD_GRAYSCALE
)

# guardar la imagen descifrada
cv2.imwrite('ruta/de/la/imagen_descifrada.jpg', img_descifrada)
