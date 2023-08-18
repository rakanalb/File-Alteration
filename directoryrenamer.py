import os
import pandas as pd

# Establish directory
file_dir = r'/Users/rakan/Coding_Projects/'
files = os.listdir(file_dir)

# Could probably use os.path.join in line 10.
for i in files:
    if '_' in i:
        # Replace the current iterated 'file' with itself but with a space instead of _s.
        i = os.rename(file_dir + i, file_dir + i.replace('_', ' '))
    else:
        print("Your files are already underscored.")

# Sanity check
df = pd.DataFrame(files)
print(df)