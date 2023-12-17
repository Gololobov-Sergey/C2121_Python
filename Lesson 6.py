import os

path = "d:\\inst"
path = os.path.normpath(path)

'''for path, dirnames, filename in os.walk(path):
    print(f"path - {path}")
    print(f"dirs - {dirnames}")
    print(f"fileas - {filename}")'''

'''dir = "111"
path = os.path.join(path, dir)
print(path)
os.mkdir(path)'''

'''print(os.path.exists(path))
print(os.path.isabs(path))
print(os.path.isdir(path))
print(os.path.isfile(path))'''

'''file = open("text.txt", "w", encoding="utf-8")
file.write("Слава Україні!")
file.close()'''

'''file = open("text.txt", "a", encoding="utf-8")
file.write("Слава Україні!\n")
file.close()'''

'''file = open("text.txt", "r", encoding="utf-8")
row = file.readlines()
print(row)
#print(file.read())
file.close()'''

'''with open("text.txt", "r", encoding="utf-8") as file:
    print(file.read())'''

#print(os.path.getctime("text.txt"))

def spy(path):
    path = os.path.normpath(path)
    result = {"dirs":[], "files":[]}
    for p, dirnames, filenams in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
        for file in filenams:
            result["files"].append(file)
        result["dirs"].sort()
        result["files"].sort()
        with open("spy.txt", "w", encoding="utf-8") as file:
            file.write(f"PATH: {path:-<50}\n")
            file.write("{:-<50}\n".format("Directories:"))
            for dir in result["dirs"]:
                file.write(f"\t[{str.upper(dir)}]\n")
            file.write("{:-<50}\n".format("Files:"))
            for files in result["files"]:
                file.write(f"\t{files}\n")



spy(path)