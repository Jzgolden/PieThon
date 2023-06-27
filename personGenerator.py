#firstName = "J'kari'ee"
#lastName = "Golden" 
#age = 24

#print("Next year's age equals: ", age + 1, type(age))
#print("First name equals: ", firstName, type(firstName))
#print("Last name equals: ", lastName, type(lastName))

class Person:
  firstName = "J'kari'ee"
  lastName = "Golden"
  age = 24
  phone = 1231231234
  absent = False
  city = "Charlotte"





jkarieeg = Person ()
#print(jkarieeg.city)

class AdvancedPerson:
  def __init__(self, firstName, lastName, age, phone, absent, city):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.phone = phone
    self.abset = absent
    self.city = city

jkarieeg = AdvancedPerson("J'kari'ee", "Golden", 24, 1231231234, False, "Charlotte")
print(jkarieeg.age)
print(jkarieeg.phone)