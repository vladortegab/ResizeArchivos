#Importa la librería OpenCV y os:
import cv2
import os

# Especifica la ruta de la carpeta que contiene las imágenes, Cambiala por el nombre de la carpeta
ruta_imagenes = "MANZANA"

#ruta_imagenes = Cambiala por el nombre de tu carpeta con las imágenes


# Especifica la nueva dimensión a la que se van a redimensionar las imágenes:
nueva_dimension = (64, 64)

# Especifica la ruta de la carpeta de salida:
ruta_salida = "RESIZE_IMAGENES_SALIDA/MANZANA"
#ruta_salida = Cambiala por el nombre de tu carpeta con las imágenes de salida

# Crea la carpeta de salida si no existe:
if not os.path.exists(ruta_salida):
    os.makedirs(ruta_salida)

# Recorre cada imagen en la carpeta y aplica el resize:
for nombre_imagen in os.listdir(ruta_imagenes):
    ruta_imagen = os.path.join(ruta_imagenes, nombre_imagen)
    imagen = cv2.imread(ruta_imagen)
    imagen_redimensionada = cv2.resize(imagen, nueva_dimension)
    ruta_salida_imagen = os.path.join(ruta_salida, nombre_imagen)
    cv2.imwrite(ruta_salida_imagen, imagen_redimensionada)
