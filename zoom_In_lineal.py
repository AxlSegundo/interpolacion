import cv2

def linear_interpolation(image, scale_factor):
    # Calcular las dimensiones de la nueva imagen
    dim1_new = int(image.shape[0] * scale_factor)
    dim2_new = int(image.shape[1] * scale_factor)
    
    # Redimensionar la imagen utilizando interpolación lineal
    resized_image = cv2.resize(image, (dim2_new, dim1_new), interpolation=cv2.INTER_LINEAR)
    
    return resized_image

# Cargar la imagen
image = cv2.imread('IMG/perro.jpeg')

# Factor de escala para el zoom
scale_factor = 2

# Aplicar interpolación lineal para redimensionar la imagen
resized_image = linear_interpolation(image, scale_factor)

# Mostrar la imagen original y la redimensionada
cv2.imshow('Original', image)
cv2.imshow('Resized', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
