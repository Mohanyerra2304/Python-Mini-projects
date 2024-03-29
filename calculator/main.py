def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n2/n1

def modulos(n1,n2):
  return n2%n1

operations = {
    '+':add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '%': modulos
  }
def calculator():

    num1 = float(input("Enter the first number? : "))
    for operation in operations:
      print(operation)
    should_continue = True
    while(should_continue):
        operation_symbol = input("pick an operation from the above line: ")
        num2 = float(input("Enter the next number? : "))
       
        calulation_function = operations[operation_symbol]
        answer = calulation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if(input(f"Do you want to continue with {answer} type 'y'to continue 'n' for fresh start: ")=="y"):
          num1=answer
        else:
          should_continue=False
          print()
          print("-----------------------------------------------------------------")
          calculator()
calculator()