# Compare 2 numbers from user and determine if it is greater, less, or equal to eachother

# Step 1: Declare 2 variables for the input of the USER. Variables only can accept integers
try: 
  pi1 = int(input("Player 1, please enter a number: "))
  pi2 = int(input("Player 2, please enter a number: "))

# Step 2: Compare the variables using an If statement.
# Step 3: Print statement based on results
  if pi1 < pi2:
    print(pi1, "is less than", pi2)

  elif pi1 > pi2: 
    print(pi1, "is greater than", pi2)

  else:
    print(pi1, "is equal to", pi2)

except:
  print("Invalid entry. Try again later :(")
