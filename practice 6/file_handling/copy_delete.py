import shutil
import os


source_file = "sample.txt"
copy_file = "sample_copy.txt"
backup_file = "sample_backup.txt"

shutil.copy(source_file, copy_file)
shutil.copy(source_file, backup_file)

filename = "sample_copy.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} deleted.")
else:
    print(f"{filename} doesnt exist.")