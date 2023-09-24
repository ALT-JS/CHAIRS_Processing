import os

# directory: /nas/shared_folders
directory = "W:\ho_datasets\CHAIRS\AHOI_Data\AHOI_ROOT\Meshes_wt"

# Get a list of all .obj files in the directory
obj_files = [f for f in os.listdir(directory) if f.endswith('.obj')]

# Define the name of the output .obj file
output_file_name = "combined.obj"

# Initialize variables to hold vertex and face data
vertices = []
faces = []
vertex_offset = 0

# Loop over each .obj file and read the vertices and faces
for obj_file in obj_files:
    with open(os.path.join(directory, obj_file), 'r') as file:
        for line in file.readlines():
            if line.startswith('v '):  # vertex
                vertices.append(line)
            elif line.startswith('f '):  # face
                # Adjust the vertex indices in face definitions
                adjusted_face = 'f ' + ' '.join([str(int(index.split('/')[0]) + vertex_offset) + index[index.find('/'):] for index in line[2:].split()])
                faces.append(adjusted_face)
                
    # Update the vertex offset for the next file
    vertex_offset += len([v for v in vertices if v.startswith('v ')])

# Write the combined data to the output file
with open(output_file_name, 'w') as file:
    file.writelines(vertices)
    file.writelines(faces)

print(f"Combined {len(obj_files)} .obj files into {output_file_name}")
