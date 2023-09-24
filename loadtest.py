import numpy as np
import json
import math

# dataset = np.load("Y:\ho_datasets\CHAIRS\AHOI_Data\DATA_FOLDER\object_rotation.npy")
dataset = np.load("object_location.npy")
with open("object2frame.json", "r") as jsonF:
    frame_dict = json.load(jsonF)
with open("infer.txt", "w") as inferF:
    for obj in frame_dict.keys():
        datas = dataset[frame_dict[obj]]
        inferF.write(str(obj)+" :\n")
        for data in datas:
            if math.isnan(data[0]):
                inferF.write("N ")
            else:
                inferF.write("Y ")
        inferF.write('\n')


# np.savetxt("obj_rotation.txt", dataset)