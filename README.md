# CHAIRS_Processing

Credits to: [Koyui](https://github.com/Koyui)

This repository can help you to generate a ground-truth of the objects in the CHAIRS dataset. It also provides our clear and verified inference to the unknown information in the dataset.

**infer.py** : About how we infer the labels corresponding to parts of the chairs.

**frame_statics.py**: To generate frame info for each object.

**transform.py**: To transform parts of the chairs with its corresponding translation and rotation.

**test.py**: To combine parts of the chair into an intact one.

All the things in the CHAIRS dataset is tangled and packed into several massive npy files, to make the matters worse, it didn't provide much useful information in both its paper and project pages.

It took me and Koyui a considerable amount of time to sort and understand the whole dataset.
