# Create list of names
# As per stakeholder, add functionality to input and add names
# Pick random name
# Print countdown before name
# Print name with emoji
# Remove name after it gets picked
# Ask to pick name or stop

import random
from time import sleep
import emoji

classNames = []

done = False
while done != True:
  name = input("Enter name or Done to complete list: ")
  if name == "Done":
    done = True
  else:
    classNames.append(name)
print(classNames)

def pickName(list):
  selection = random.choice(classNames)
  count = 10
  while count > 0:
    print(count)
    #sleep(1)
    count -= 1

  print(emoji.emojize(":woman_raising_hand:"))
  print(emoji.emojize(":heart_on_fire:"))
  print(selection)

  classNames.remove(selection)
  print(classNames)

pick = ""
while pick != "Stop":
  pick = input("Pick name? ")
  try:
    pickName(classNames)
  except IndexError:
    print("There are no other names to pick from!")
  finally:
  print("Thanks for using our prgram!")




