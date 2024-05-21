import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer la imagen
imagen = cv2.imread('IMG/perro.jpeg')  # Reemplaza 'ruta/a/tu/imagen.jpg' con la ruta a tu imagen
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB para mostrar correctamente con matplotlib

# Redimensionar la imagen aumentando la altura al doble
altura_nueva_aumentada = int(imagen.shape[0] * 1.5)
imagen_aumentada_altura = cv2.resize(imagen_rgb, (imagen.shape[1], altura_nueva_aumentada), interpolation=cv2.INTER_LINEAR)

# Redimensionar la imagen reduciendo la altura a la mitad
altura_nueva_reducida = int(imagen.shape[0] * 0.5)
imagen_reducida_altura = cv2.resize(imagen_rgb, (imagen.shape[1], altura_nueva_reducida), interpolation=cv2.INTER_LINEAR)

# Mostrar las imágenes
plt.figure(figsize=(15, 5))

# Imagen original
plt.subplot(1, 3, 1)
plt.title('Imagen Original')
plt.imshow(imagen_rgb)
plt.axis('off')

# Imagen con altura aumentada
plt.subplot(1, 3, 2)
plt.title('Altura Aumentada')
plt.imshow(imagen_aumentada_altura)
plt.axis('off')

# Imagen con altura reducida
plt.subplot(1, 3, 3)
plt.title('Altura Reducida')
plt.imshow(imagen_reducida_altura)
plt.axis('off')

plt.show()
