import numpy as np

dataset = np.load("W:\ho_datasets\CHAIRS\AHOI_Data\DATA_FOLDER\object_root_location.npy")

np.savetxt("obj_root_location.txt", dataset)