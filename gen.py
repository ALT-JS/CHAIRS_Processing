import numpy as np

data1 = np.load('object_id.npy')
data2 = np.load('img_name.npy')

len = np.size(data1)
ans = []
i = 0; j = data1[0]; temp = [j]
while i < len :
    mark = data2[i][0:4]
    if data1[i] != j :
        ans.append(temp)
        j = data1[i]
        temp = [j]
    count = 0
    for k in temp :
        if mark == k :
            count += 1
    if count == 0:
        temp.append(mark)
    i += 1
    
# print(ans)
# np.savetxt("correlation.csv", ans, delimiter=",", fmt = '%s')
import pandas as pd

df = pd.DataFrame(ans)
df.to_csv('myfile.csv', index=False)