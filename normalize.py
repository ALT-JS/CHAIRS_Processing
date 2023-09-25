import os
import torch
obj_path = r'Y:\ho_datasets\CHAIRS\object_GT\64\123536\combined.obj'
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
def normalize(objTemp):
    Ano = objTemp.t()
    mean_tl = (torch.mean(Ano[0]), torch.mean(Ano[1]), torch.mean(Ano[2]))
    mean_tl = torch.tensor(mean_tl)
    objTemp -= mean_tl
    return objTemp
vertices = load_obj(obj_path)
new_verts = normalize(vertices)
with open(obj_path.replace('combined', 'normalized'), 'w') as objW:
    for v_info in new_verts:
        objW.write(f'v {v_info[0]} {v_info[1]} {v_info[2]}\n')
    with open(obj_path, 'r') as objR:
        lines = objR.readlines()
        for line in lines:
            if line.startswith('f '):
                objW.write(line)

