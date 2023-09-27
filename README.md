# CHAIRS_Processing

Credits to: [Koyui](https://github.com/Koyui)

**correlations.csv**: The first column is the object_id, and the corresponding row of every object_id is the folders that contain this object in IMG_FOLDER. Sorry for the jankiness of it.

**infer.py**: This program is about how we infer the labels that correspondin to parts of the CHAIRS.

**frame_statics.py**: This program can generate frame info for each object.

**transform.py**: This program can transform parts of the CHAIRS object with its corresponding translation and rotation given in the npy files.

**test.py**: This program can combine parts of the CHAIRS object into an intact one.

**normalize.py**: We use it to shift the regenerated object back to the original point for tests, **the correct way to reiterate CHAIRS should be using root_location/rotation npy file to relocate combined objects**.
