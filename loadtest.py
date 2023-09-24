import numpy as np

dataset = np.load("W:\ho_datasets\CHAIRS\AHOI_Data\DATA_FOLDER\object_root_rotation.npy")

np.savetxt("obj_root_rotation.txt", dataset)