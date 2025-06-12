import gzip
import shutil
import scipy.io

# Step 1: Extract the .mat file from .gz
input_path = r'C:\Users\KC-USER\Downloads\0154423_struc_CM (3).mat.gz'
output_path = r'C:\Users\KC-USER\Downloads\0154423_struc_CM (3).mat'

with gzip.open(input_path, 'rb') as f_in:
    with open(output_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print(f"File extracted to {output_path}")

# Step 2: Load the .mat file using scipy.io
mat_data = scipy.io.loadmat(output_path)

# Step 3: Print keys (variables in the .mat file)
print(mat_data.keys())

# Optional: Access a specific variable
# print(mat_data['your_variable'])
