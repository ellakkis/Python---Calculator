from art import logo

# Calculator

def add(a, b):
  """A functin tat take two numbers and return their sum"""
  return a + b

# Subtraction
def subtract(a, b):
  """A functin tat take two numbers and return their subtraction"""
  return a - b

# Multiply
def muliply(a, b):
  """A functin tat take two numbers and return a * b"""
  return a * b

# Divide
def devide(a, b):
  """A functin tat take two numbers and return a / b"""
  return a / b

# Dictionary containing the 4 operations
operations = {
  "+": add,
  "-": subtract,
  "*": muliply,
  "/": devide
}

def calculator():
  print(logo)

  
    
  # get user input
  num1 = float(input("What's the first number?: "))
  num2 = float(input("What's the second number?: "))
  print("What operation you wnat to do?: ")
  print(" ".join(operations), end = "\n")
  user_op = input()

  # carry the calculation and present result
  result = operations[user_op](num1, num2)
  print(f"{num1} {user_op} {num2} = {result}")

  calculate_another = True
  while calculate_another:
    calculate_more = input(f"Type 'y to continue calculating with {result}, or 'n to exit: ").lower()
    if calculate_more == "y":
      calculate_another = True
      first_num = result
      second_num = float(input("What's the next number?: "))
      new_user_op = input("Pick an operation: ")
      result = operations[new_user_op](first_num, second_num)
      print(f"{first_num} {new_user_op} {second_num} = {result}")
    else:
      calculate_another = False
      
    
  
calculator()