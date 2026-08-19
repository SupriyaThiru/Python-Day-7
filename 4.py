file = open("data.txt", "r")
lines = file.readlines()
print("number of lines in the file:", len(lines))
file.close()