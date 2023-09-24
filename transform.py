import numpy as np
import os
import json
import torch
dataset_loc = np.load("W:\ho_datasets\CHAIRS\AHOI_Data\DATA_FOLDER\object_location.npy")
dataset_rot = np.load("W:\ho_datasets\CHAIRS\AHOI_Data\DATA_FOLDER\object_rotation.npy")
# directory: /nas/shared_folders
print("Loading Complete.")
directory = r"W:\ho_datasets\CHAIRS\AHOI_Data\AHOI_ROOT\Meshes_wt\30"
output = r'W:\ho_datasets\CHAIRS\object_GT\30'
def euler2matrix(rot):
    alpha = rot[0]
    beta = rot[1]
    gamma = rot[2]
    Rx = np.array([[1, 0, 0], [0, np.cos(alpha), -np.sin(alpha)], [0, np.sin(alpha), np.cos(alpha)]])
    Ry = np.array([[np.cos(beta), 0, np.sin(beta)], [0, 1, 0], [-np.sin(beta), 0, np.cos(beta)]])
    Rz = np.array([[np.cos(gamma), -np.sin(gamma), 0], [np.sin(gamma), np.cos(gamma), 0], [0, 0, 1]])
    rotation_matrix = Rz.dot(Ry).dot(Rx)
    return rotation_matrix

def transform_template(objTemp,trans,rot):
    rot = euler2matrix(np.array(rot))
    rot = torch.tensor(rot, dtype=torch.float)
    objTemp = torch.mm(objTemp,rot.t())
    trans = torch.tensor(trans, dtype=torch.float)
    objTemp += trans
    return objTemp

def load_obj(objFn):
    vertices = None
    with open(objFn, 'r') as objF:
        lines = objF.readlines()
        for line in lines:
            if line[0] == 'v':
                now_vertices = torch.tensor(list(map(float, line.split()[1:]))).unsqueeze(0)
                if vertices is None:
                    vertices = now_vertices
                else:
                    vertices = torch.cat((vertices, now_vertices), dim=0)
        vertices = vertices
        return vertices

# Get a list of all .obj files in the directory
obj_files = [f for f in os.listdir(directory) if f.endswith('.obj')]
with open("object2frame.json", 'r') as jsonF: 
    id_dict = json.load(jsonF)
with open("infer.json", 'r') as jsonF:
    infer_dict = json.load(jsonF)
frame_info = id_dict[str(30)]
for idx, start_frame in enumerate(frame_info['start']):
    start_frame = start_frame-1
    end_frame = frame_info['ends'][idx]-1
    for frame in range(start_frame, end_frame):
        output_dir = os.path.join(output, str(frame))
        os.makedirs(output_dir, exist_ok=True)
        for obj in obj_files:
            vertices = load_obj(os.path.join(directory, obj))
            cnt = infer_dict[obj]
            cnt -= 1
            new_obj = transform_template(vertices, dataset_loc[frame][cnt], dataset_rot[frame][cnt])
            with open(os.path.join(output_dir, obj.replace('.obj','_new.obj')), 'w') as objF:
                for v_info in new_obj:
                    objF.write(f'v {v_info[0]} {v_info[1]} {v_info[2]}\n')
                with open(os.path.join(directory,obj), 'r') as objR:
                    lines = objR.readlines()
                    for line in lines:
                        if line.startswith('f '):
                            objF.write(line)

            print(obj+"_location: ",dataset_loc[frame][cnt])