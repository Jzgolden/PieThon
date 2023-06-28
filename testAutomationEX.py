# Test automation example: 

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

# TESTS
try:
    assert add(2, 2) == 4
    print(True)
except AssertionError:
    print(False)

try:
    assert multiply(2, 5) == 10
    print(True)
except AssertionError:
    print(False)

try:
    assert subtract(10, 4) == 6
    print(True)
except AssertionError:
    print(False)

try:
    assert divide(10, 2) == 5
    print(True)
except AssertionError:
    print(False)


# Single block example:

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

# TESTS

try:
    assert add(2, 2) == 4
    assert multiply(2, 5) == 10
    assert subtract(10, 4) == 6
    assert divide(10, 2) == 5
    print("All tests passed!")
except AssertionError:
    print("One or more tests failed.")



