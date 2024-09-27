def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

first_num = float(input("Enter the First number: "))
for symbol in operations:
    print(symbol)
operator = input("Choose the operation: +, -, *, or, / ")
second_num = float(input("Enter the Second number: "))
answer = operations[operator](first_num,second_num)
print(f"{first_num} {operator} {second_num} = {answer}")

next_calc = input("Would you like to continue with the previous value? Y for yes N for no: ")

if next_calc == "y":
    first_num = answer
    operator = input("Choose the operation: +, -, *, or, / ")
    second_num = float(input("Enter the Second number: "))
    answer = operations[operator](first_num, second_num)
    print(f"{first_num} {operator} {second_num} = {answer}")

else:
    print("Bye")



