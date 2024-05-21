import cv2

def bilinear_interpolation(image, scale_factor):
    # Calcular las dimensiones de la nueva imagen
    dim1_new = int(image.shape[0] * scale_factor)
    dim2_new = int(image.shape[1] * scale_factor)
    
    # Redimensionar la imagen utilizando el algoritmo bilineal
    resized_image = cv2.resize(image, (dim2_new, dim1_new), interpolation=cv2.INTER_LINEAR)
    
    return resized_image

# Cargar la imagen
image = cv2.imread('IMG/perro.jpeg')

# Factor de escala para el zoom (aumento)
scale_factor_zoom_in = 2

# Factor de escala para el zoom (disminución)
scale_factor_zoom_out = 0.5

# Aplicar interpolación bilineal para redimensionar la imagen con zoom (aumento)
resized_image_zoom_in = bilinear_interpolation(image, scale_factor_zoom_in)

# Aplicar interpolación bilineal para redimensionar la imagen con zoom (disminución)
resized_image_zoom_out = bilinear_interpolation(image, scale_factor_zoom_out)

# Mostrar la imagen original, la imagen con zoom (aumento) y la imagen con zoom (disminución)
cv2.imshow('Original', image)
cv2.imshow('Zoom (Aumento)', resized_image_zoom_in)
cv2.imshow('Zoom (Disminución)', resized_image_zoom_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
