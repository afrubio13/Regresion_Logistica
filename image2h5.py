from PIL import Image
import numpy as np
import os
import h5py

# Función para convertir una imagen en un array de numpy
def image_to_array(image_path, size=(28, 28)):
    with Image.open(image_path) as img:
        # Convertir la imagen a escala de grises
        img = img.convert('L')
        # Redimensionar la imagen
        img = img.resize(size)
        # Convertir la imagen a un array de numpy
        img_array = np.array(img)
    return img_array

# Directorio de imágenes
image_dir = 'imagenes'

# Listas para almacenar los datos y etiquetas
data = []
labels = []

# Leer todas las imágenes en el directorio
for filename in os.listdir(image_dir):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        image_path = os.path.join(image_dir, filename)
        img_array = image_to_array(image_path)
        data.append(img_array)  # No aplanamos la imagen para conservar su forma
        labels.append(filename)  # Puedes cambiar esto para usar etiquetas más significativas

# Convertir las listas a arrays de numpy
data = np.array(data)
labels = np.array(labels)

# Guardar los datos en un archivo .h5
with h5py.File('dataset.h5', 'w') as h5f:
    h5f.create_dataset('images', data=data)
    h5f.create_dataset('labels', data=labels.astype('S'))  # Convertir etiquetas a string

print("Dataset guardado exitosamente en formato HDF5")
