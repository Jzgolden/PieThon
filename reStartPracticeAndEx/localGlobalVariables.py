# Local variable example: 

def greet():
  # local variable
  message = 'Hello'

  print('Local', message)

greet()

# "Message" is apart of the def function and can not be called. Will give error. 
print(message)


# Global variable example: 

def greet():
  # Local variable
  print('Local', message)

greet()
print('Global', message)



# Notes: The difference between global and local variables is the indentation. Global variables are defined outside of any function or block making them accessible throughout the entire program. Local variables are declared within a specific function or block and have a limited scope.