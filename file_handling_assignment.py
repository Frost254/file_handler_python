#Create a new file

f = open("my_file.txt", "a")
f.write("\n Now the file has more content!")
f.write("\n 12")
f.write("\n Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("my_file.txt", "r")
print(f.read())
f.close()

try:
    f = open("my_file.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: can\'t find file or read data")
except PermissionError:
    print("Error: can\'t access file or read data")
