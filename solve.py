import cv2

def remove_noise(image):

    # Код с применением фильтра Гаусса
    # gaussian_kernel_size = (5, 5)
    # sigma_x = 0
    # filtered_image = cv2.GaussianBlur(image, kernel_size, sigma_x)

    median_kernel_size = 5
    filtered_image = cv2.medianBlur(image, median_kernel_size)

    return filtered_image

input_image = cv2.imread('input_image.tiff', cv2.IMREAD_UNCHANGED)

filtered_image = remove_noise(input_image)

cv2.imwrite('output_image.tiff', filtered_image)
