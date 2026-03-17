import os

path = "practice_folder/subfolder1/subfolder2"
os.makedirs(path, exist_ok=True)
path = "practice_folder"

print("Содержимое папки:")
for item in os.listdir(path):
    print(item)
    
target_extension = ".txt"

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(target_extension):
            print(os.path.join(root, file))