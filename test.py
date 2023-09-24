### If it works, author: Koyui
### If not, author: ALT
import os

# directory: /nas/shared_folders
work_dir = r'W:\ho_datasets\CHAIRS\object_GT\30'
directories = [f for f in os.listdir(work_dir)]
for idx, directory in enumerate(directories):
    directory = os.path.join(work_dir, directory)
    # Get a list of all .obj files in the directory
    obj_files = [f for f in os.listdir(directory) if f.endswith('.obj') and f!="combined.obj"]

    # Define the name of the output .obj file
    output_file_name = os.path.join(directory, "combined.obj")
    if os.path.exists(output_file_name):
        continue

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
                    adjusted_face = 'f ' + ' '.join([str(int(index) + vertex_offset) for index in line[2:].split()])+'\n'
                    faces.append(adjusted_face)
                    
        # Update the vertex offset for the next file
        vertex_offset += len([v for v in vertices if v.startswith('v ')])

    # Write the combined data to the output file
    with open(output_file_name, 'w') as file:
        file.writelines(vertices)
        file.writelines(faces)
    if idx % 250 == 0:
        print(f"from {directory} has Combined {len(obj_files)*1000} .obj files into {output_file_name}")
        print(f'{idx}/{len(directories)}')
