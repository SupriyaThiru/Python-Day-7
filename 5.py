file = open("data.txt", "r")
words = file.read().split()
print("number of words in the file:", len(words))
file.close()