# Create a class of person with multiple properties
class AdvancedPerson:
    def __init__(self, firstName, lastName, age, areaCode, city, birthYear, zipCode, favEmail):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.areaCode = areaCode
        self.city = city
        self.birthYear = birthYear
        self.zipCode = zipCode
        self.favEmail = favEmail

firstNameUser = input("Enter your first name: ")
lastNameUser = input("Enter your last name: ")
ageUser = input("Enter your age: ")
areaCodeUser = input("Enter your area code: ")
cityUser = input("Enter your city: ")
birthYearUser = input("Enter your birth year: ")
favEmailUser = input("Enter your favorite email provider: ")
zipcodeUser = input("Enter your zip code: ")

# Generate a person with all properties
person = AdvancedPerson(firstNameUser, lastNameUser, ageUser, areaCodeUser, cityUser, birthYearUser, zipcodeUser, favEmailUser)

# Create a function that uses 3 properties from the person and creates an email address
def emailGenerator(val1, val2, val3, favEmail):
    email = val1 + val2 + val3 + "@" + favEmail + ".com"
    return email

# Generate email using person's properties
generatedEmail = emailGenerator(person.firstName, person.city, person.birthYear, person.favEmail)
print(generatedEmail)
