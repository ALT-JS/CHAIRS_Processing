import os
import numpy as np
import json

id_info = np.load("object_id.npy")
img_info = np.load("img_name.npy")

object2frame = {}
for id in range(len(id_info)-1):
    if(id_info[id]!=id_info[id+1]):
        object2frame[str(id_info[id])] = {"start":[],"ends":[]}
object2frame['116']['start'].append(1)
for id in range(len(id_info)-1):
    if(id_info[id]!=id_info[id+1]):
        print(id_info[id],":",id)
        object2frame[str(id_info[id])]['ends'].append(id+1)
        object2frame[str(id_info[id+1])]['start'].append(id+2)
object2frame[str(id_info[len(id_info)-1])]['ends'].append(len(id_info))
with open("object2frame.json",'w') as jsonF:
    json.dump(object2frame, jsonF, indent=4) 
        
        

