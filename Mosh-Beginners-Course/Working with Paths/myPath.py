# You can use absolute or relative paths, if you put path() this will be the current directory
from pathlib import Path

# check for existence
path = Path("g:/temp/emails")
print(path.exists())

# make a directory
path = Path("g:/temp/emails")
print(path.mkdir())

# delete a directory
path = Path("g:/temp/emails")
print(path.rmdir())

# find all files in the current directory
path2 = Path()
for file in path.glob('*.py'):
    print(file)