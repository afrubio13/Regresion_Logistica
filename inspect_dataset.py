import h5py

def inspect_hdf5_file(file_path):
    with h5py.File(file_path, 'r') as f:
        print("Contenido del archivo HDF5:")
        f.visit(print)
# Ruta a tu archivo HDF5
file_path = 'datasets/train_catvnoncat.h5'

# Inspeccionar el archivo
inspect_hdf5_file(file_path)