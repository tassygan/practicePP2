import shutil
import os

os.makedirs("folderA", exist_ok=True)
os.makedirs("folderB", exist_ok=True)

with open("folderA/test.txt", "w", encoding="utf-8") as f:
    f.write("folderA")

shutil.copy("folderA/test.txt", "folderB/test_copy.txt")
print("file copied to folderB.")

shutil.move("folderA/test.txt", "folderB/test_moved.txt")
print("file moved to folderB.")