from Crypto.Cipher import AES
import os


def encrypt_file(key, filename):
    chunksize = 64 * 1024
    outputFile = filename[:-4] + ".encrypted"
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_OFB, IV)
    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))
                outfile.write(encryptor.encrypt(chunk))
