# Try Except :
def divide_five_by(number):
  try:
    value = 5/number
  except ZeroDivisionError:
    print("Cannot divide by zero")
    value = 1
  return value

print(divide_five_by(10))



# Try Except Except
try:
  even_numbers = [2, 4, 6, 8]
  print(even_numbers[6])
  
except IndexError:
  print("Index out of bounds for this list")

except ZeroDivisionError:
  print("NO")





# Try Except Else
try:
  num = int(input("Enter an even number: "))
  assert num % 2 == 0

except:
  print("This is not an even number!")

else:
  reciprocal = 1/num
  print(reciprocal)




# Try Except Finally
try: 
  numerator = 10
  denominator = 0

  result = numerator / denominator

  print(result)
except ZeroDivisionError:
  print("Error: Denominator cannot be zero")
finally:
  print("Regardless of anything else, the finally block will ALWAYS run")


