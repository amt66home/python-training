import glob
print("All xlsx and txt files")
extensions = ('*.doc', '*.txt')
files_list = []
for ext in extensions:
    files_list.extend(glob.glob(ext))
print(files_list)
