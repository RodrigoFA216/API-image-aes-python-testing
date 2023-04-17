import cv2
import numpy as np

# función que agregará ceros a la izquierda para completar el octeto


def complete_octet(bin_str):
    # Calcula la cantidad de ceros que se deben agregar
    num_zeros = 8 - len(bin_str)
    # Agrega los ceros a la izquierda del número binario
    return "0" * num_zeros + bin_str


async def hide_img(path_y, path_a, path_b):
    Y = cv2.imread(path_y, cv2.IMREAD_GRAYSCALE)
    A = cv2.imread(path_a, cv2.IMREAD_GRAYSCALE)
    B = cv2.imread(path_b, cv2.IMREAD_GRAYSCALE)
    # Height alto Width ancho
    h, w = Y.shape
    ah, aw = A.shape
    bh, bw = B.shape
    Y_vector = Y.flatten()
    A_vector = A.flatten()
    B_vector = B.flatten()
    arr = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
    bin_func = np.vectorize(
        lambda x: complete_octet(format(x, "b"))
    )  # combierte todo a binario
    int_func = np.vectorize(lambda x: int(x, 2))  # combierte todo a decmal
    array = bin_func(arr)
    nexts = int_func(array)
    # print(arr == nexts)
    Y_vec_bin = bin_func(Y_vector)
    A_vec_bin = bin_func(A_vector)
    B_vec_bin = bin_func(B_vector)
    # print(type(A_vec_bin[0]))
