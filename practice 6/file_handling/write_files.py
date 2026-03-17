with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("David, 21\nEva, 23\n")

with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.read())