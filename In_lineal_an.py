import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer la imagen
imagen = cv2.imread('IMG/perro.jpeg')  # Reemplaza 'ruta/a/tu/imagen.jpg' con la ruta a tu imagen
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB para mostrar correctamente con matplotlib

# Redimensionar la imagen aumentando la anchura al doble
ancho_nuevo_aumentado = int(imagen.shape[1] * 1.5)
imagen_aumentada_ancho = cv2.resize(imagen_rgb, (ancho_nuevo_aumentado, imagen.shape[0]), interpolation=cv2.INTER_LINEAR)
# Redimensionar la imagen reduciendo la anchura a la mitad
ancho_nuevo_reducido = int(imagen.shape[1] * 0.7)
imagen_reducida_ancho = cv2.resize(imagen_rgb, (ancho_nuevo_reducido, imagen.shape[0]), interpolation=cv2.INTER_LINEAR)


# Mostrar las imágenes
plt.figure(figsize=(15, 5))

# Imagen original
plt.subplot(1, 3, 1)
plt.title('Imagen Original')
plt.imshow(imagen_rgb)
plt.axis('off')

# Imagen con anchura aumentada
plt.subplot(1, 3, 2)
plt.title('Anchura Aumentada')
plt.imshow(imagen_aumentada_ancho)
plt.axis('off')

# Imagen con anchura reducida
plt.subplot(1, 3, 3)
plt.title('Anchura Reducida')
plt.imshow(imagen_reducida_ancho)
plt.axis('off')

plt.show()
