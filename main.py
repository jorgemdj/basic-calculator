import os
from art import logo


def sum(a, b):
  return a+b
  
def sub(a, b):
  return a-b
  
def mult(a, b):
  return a*b
  
def div(a, b):
  return a/b

operations = {
  "+": sum,
  "-": sub,
  "*": mult,
  "/": div
}



loop = True

while loop == True:
  setup = 0
  while setup != "ok":
    setup = 0
    print(logo)
    first_number = float(input("What's the first number?: "))
    for symbol in operations:
      print(symbol)
    operation = input("Pick an operation: ")
  
    if operation not in operations:
      print("Operation symbol didn't match. Please, try again.")
      break
    else:
      second_number = float(input("What's the next number?: "))
      result = operations[operation](first_number,second_number)
      
      print(f"{first_number} {operation} {second_number} = {result}")
      setup = "ok"

    restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if restart == 'n':
      new_calculation = False
      os.system('cls')

    else:
      setup = 0
      new_calculation = True
      
    while new_calculation == True:
      
      setup = 0
      while setup != "ok":
        operation = input("Pick an operation: ")
        if operation not in operations:
          print("Operation symbol didn't match. Please, try again.")
          break
          
        else:
          second_number = float(input("What's the next number?: "))
          result_print = result
          result = operations[operation](result,second_number)
          print(f"{result_print} {operation} {second_number} = {result}")
          setup = "ok"
    
      restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

      print(restart == 'n')
      
      if restart == 'n':
        os.system('cls')
        new_calculation = False
    