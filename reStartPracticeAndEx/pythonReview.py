# Creating and editing a new file

file1 = open("myFile.txt", "r")


print(file1.read())
print(file1.readline())
file1.close()

file2 = open("myFile.txt", "w")
add = "Absorbant and yellow and porous is he"
file2.write(add)
file2.close()

#--------------------------------------------------------

file = input("Enter file name: ")

try:
  open(file + "txt")
except FileNotFoundError:
  print("Geht Nicht")



try:
  open(file + "txt")
except FileNotFoundError:
  print("Geht Nicht")
finally:
  print("Thanks for using our app")



try:
  print(1/0)
except ZeroDivisionError: 
  print("Geht Nicht")



try:
  open("FileThatDoesNotExist.txt")
except FileNotFoundError:
  print("Geht Nicht")



raise MemoryError("Running out of memory, buy a better rig to play games with a good FPS")

#--------------------------------------------------------

cities = ["Charlotte", "Tashkent", "Hampton", "Milan", "Gastonia"]

cities.insert(3, "Charleston")
print(cities)

cities.remove("Hampton")
print(cities)

cities.pop(2)
print(cities)

#--------------------------------------------------------

x = False

while x == False:
  user_write = input("Yes / No")
  if user_write == "No":
    x = True
  elif user_write == "Yes":
    print ("Good job")
  
