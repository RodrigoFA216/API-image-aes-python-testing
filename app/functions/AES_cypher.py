import cv2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def cypher_image(key, vector, path, name):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    aes = AES.new(key, AES.MODE_OFB, vector)
    # Aplicar el cifrado
    img_cifrada = aes.encrypt(pad(img.tobytes(), AES.block_size))
    with open(path[:-len(name)]+name[:-4]+'-cif'+name[-4:], 'wb') as f:
        f.write(img_cifrada)
