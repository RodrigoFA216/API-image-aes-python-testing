import cv2
import numpy as np


def embed_images_LSB(principal_path, a_path, b_path):
    # Load images
    principal = cv2.imread(principal_path, cv2.IMREAD_GRAYSCALE)
    a = cv2.imread(a_path, cv2.IMREAD_GRAYSCALE)
    b = cv2.imread(b_path, cv2.IMREAD_GRAYSCALE)

    # Get image dimensions
    h, w = principal.shape
    ah, aw = a.shape
    bh, bw = b.shape

    # Define start and end coordinates for A and B embedding
    a_start = (int(w/4), int(h/4))
    a_end = (int(w/4)+aw, int(h/4)+ah)
    b_start = (int(w/2), int(h/2))
    b_end = (int(w/2)+bw, int(h/2)+bh)

    # Embed A in LSB of principal
    for i in range(ah):
        for j in range(aw):
            pixel = bin(principal[a_start[1]+i, a_start[0]+j])[2:].zfill(8)
            pixel = pixel[:-2] + bin(a[i, j])[2:].zfill(8)[-2:]
            principal[a_start[1]+i, a_start[0]+j] = int(pixel, 2)

    # Embed B in LSB of principal
    for i in range(bh):
        for j in range(bw):
            pixel = bin(principal[b_start[1]+i, b_start[0]+j])[2:].zfill(8)
            pixel = pixel[:-2] + bin(b[i, j])[2:].zfill(8)[-2:]
            principal[b_start[1]+i, b_start[0]+j] = int(pixel, 2)

    # Create color image from YCbCr components
    principal_color = cv2.cvtColor(
        np.uint8(cv2.merge((principal, a, b))), cv2.COLOR_YCrCb2BGR)

    # Return start and end coordinates for A and B embedding
    return [a_start, a_end], [b_start, b_end], principal_color


def embed_images(principal_path, A_path, B_path):
    # Load images
    principal = cv2.imread(principal_path, cv2.IMREAD_GRAYSCALE)
    A = cv2.imread(A_path, cv2.IMREAD_GRAYSCALE)
    B = cv2.imread(B_path, cv2.IMREAD_GRAYSCALE)
    # Convert A to vector and get height and width
    A_vector = np.ravel(A)
    A_height, A_width = A.shape
    # Create empty list to store embedding start and end pixels
    embeddings = []
    # Embed A
    for i, bit in enumerate(A_vector):
        # Calculate embedding position
        x = (i // A_width) * 2
        y = (i % A_width) * 2
        # Embed bit
        principal[x, y] = (principal[x, y] & 254) | (bit & 1)
        # Check if we finished embedding A
        if i == len(A_vector) - 1:
            embeddings.append((x, y))
            embeddings.append((x + A_height * 2, y + A_width * 2))
    # Convert B to vector and get height and width
    B_vector = np.ravel(B)
    B_height, B_width = B.shape
    # Embed B
    for i, bit in enumerate(B_vector):
        # Calculate embedding position
        x = ((i // B_width) * 2) + A_height * 2
        y = (i % B_width) * 2
        # Embed bit
        principal[x, y] = (principal[x, y] & 254) | (bit & 1)
        # Check if we finished embedding B
        if i == len(B_vector) - 1:
            embeddings.append((x, y))
            embeddings.append((x + B_height * 2, y + B_width * 2))
    return embeddings


def lsb_embedding(img, data):
    """
    Function to embed data in an image using LSB technique
    """
    data_len = len(data)
    img_shape = img.shape
    channels = img_shape[2]
    # Flatten image into a 1D array
    img_flattened = img.reshape((-1, channels))
    # Embed data in the least significant bit of the last channel
    for i in range(data_len):
        img_flattened[i][-1] = data[i]
        # Reshape the flattened array back to the original image shape
        img_embedded = img_flattened.reshape(img_shape)
    return img_embedded


def lsb_extract(img, data_len):
    """
    Function to extract data from an image using LSB technique
    """
    img_shape = img.shape
    channels = img_shape[2]
    # Flatten image into a 1D array
    img_flattened = img.reshape((-1, channels))
    # Extract the least significant bit of the last channel
    data = [img_flattened[i][-1] for i in range(data_len)]
    return data


def embed_images(principal_path, a_path, b_path):
    # Load images
    img_principal = cv2.imread(principal_path, cv2.IMREAD_UNCHANGED)
    img_a = cv2.imread(a_path, cv2.IMREAD_UNCHANGED)
    img_b = cv2.imread(b_path, cv2.IMREAD_UNCHANGED)
    # Convert component Cb and Cr images to 1D arrays
    cb_data = img_a.flatten().tolist()
    cr_data = img_b.flatten().tolist()
    # Embed Cb and Cr data in the Y component image using LSB
    img_embedded = lsb_embedding(img_principal, cb_data)
    start_pixel = 0
    end_pixel = len(cb_data)
    img_embedded = lsb_embedding(img_embedded, cr_data)
    start_pixel_end = end_pixel
    end_pixel_end = len(cr_data) + end_pixel
    # Save the embedded image
    cv2.imwrite('embedded_image.png', img_embedded)
    # Return start and end pixels for each component
    return [(start_pixel, end_pixel), (start_pixel_end, end_pixel_end)]


# Example usage
start_end_pixels = embed_images('principal.png', 'a.png', 'b.png')
print(start_end_pixels)
