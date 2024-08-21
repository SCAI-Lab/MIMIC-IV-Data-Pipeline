import h5py
import numpy as np
from tqdm import tqdm
from natsort import natsorted

# Accessing and checking the saved data with a progress bar
with h5py.File('all_batches_data.h5', 'r') as h5file:
    batch_names = natsorted(list(h5file.keys()))  # Get all batch names
    for batch_name in tqdm(batch_names, desc="Loading batches"):
        print(f"Batch {batch_name}:")
        for dataset_name in h5file[batch_name].keys():
            print(f"  {dataset_name}: {h5file[batch_name][dataset_name].shape}")
