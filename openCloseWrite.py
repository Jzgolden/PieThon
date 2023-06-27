print("Here is my diary: \n")
f1 = open("jaiiDiary1.txt", "r")
print(f1.read())
f1.close()

#create a new diary
f2 = open("jaiiDiary2.txt", "w")
f2.write("xxxxxxxxxx")
f2.close()

f3 = open("jaiiDiary1.txt", "a")  # Use "a" mode to append to the file instead of overwriting it
f3.write("\nThis is a new entry to my diary")
f3.close()
