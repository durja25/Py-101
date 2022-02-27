import pandas as pd

import os


def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            # filepath = os.path.join(root, filename)
            file_paths.append(filename)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.
full_file_paths = get_filepaths('path')

# print(full_file_paths)

df = pd.read_csv('pathtocsv', dtype='str')
# Syntax to reduce the number of columns (Can use their names!)
df2_less_columns = df[['title','url']]


df2_less_columns = df2_less_columns.to_csv('original.csv', index=False)
print(df2_less_columns)

# Writing files to csv file
df = pd.DataFrame(full_file_paths)

# It will include index also
# df.to_csv('test.csv')

#Without Index
df.to_csv('dld.csv', index=False, )