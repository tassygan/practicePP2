filename = "sample.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write("Aidana, 20\n")
    f.write("Ali, 22\n")
    f.write("Kate, 19\n")


with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.read())
