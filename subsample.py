import os
import shutil
import random

random.seed(42)

# Define paths to the folders
base_folder = "Group_6_water_smooth"
train_folder = os.path.join(base_folder, "train")
subsample_train_folder = os.path.join(base_folder, "subsample_train")

# Ensure subsample_train folder exists
if not os.path.exists(subsample_train_folder):
    os.makedirs(subsample_train_folder)

if os.path.exists(subsample_train_folder):
    shutil.rmtree(subsample_train_folder)

# Define the fraction of the dataset to include in the subsample (e.g., 0.2 for 20%)
subsample_fraction = 0.05

# Iterate over class folders in the train set
for class_folder in os.listdir(train_folder):
    class_path = os.path.join(train_folder, class_folder)
    
    # Ensure it's a directory
    if os.path.isdir(class_path):
        # Create a corresponding class folder in subsample_train
        subsample_class_folder = os.path.join(subsample_train_folder, class_folder)
        if not os.path.exists(subsample_class_folder):
            os.makedirs(subsample_class_folder)
        
        # List files in the class folder
        files = os.listdir(class_path)
        
        # Calculate the number of files to include in the subsample
        num_files_subsample = int(len(files) * subsample_fraction)
        
        # Randomly select files for the subsample
        subsample_files = random.sample(files, num_files_subsample)
        
        # Copy selected files to the subsample class folder
        for file_name in subsample_files:
            file_path = os.path.join(class_path, file_name)
            shutil.copy(file_path, subsample_class_folder)

print("Subsample of the training set created successfully.")
