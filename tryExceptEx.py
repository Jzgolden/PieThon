#Try Except Examples:
def divide_five_by(number):
  try:
    value = 5/number
  except ZeroDivisioniError:
    print("No")
    value = 1
    return value


print(5/10)

