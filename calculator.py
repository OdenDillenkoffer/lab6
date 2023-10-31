first_op = input("Enter first operand:")
second_op = input("Enter second operand:")
#takes user input
print("Calculator Menu")
print("-" * 15)
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
#Calculator menu, I find using multiple print lines to be far readable
selection = input("Which operation do you want to perform?")
#Tests all valid possible inputs and does each operation
if int(selection) == 1:
    answer = float(first_op) + float(second_op)
    print("The result of the operation is", str(answer) + ". Goodbye!")
elif int(selection) == 2:
    answer = float(first_op) - float(second_op)
    print("The result of the operation is", str(answer) + ". Goodbye!")
elif int(selection) == 3:
    answer = float(first_op) * float(second_op)
    print("The result of the operation is", str(answer) + ". Goodbye!")
elif int(selection) == 4:
    answer = float(first_op) / float(second_op)
    print("The result of the operation is", str(answer) + ". Goodbye!")
else:
    print("Error: Invalid selection! Terminating program.")
#With no other possible selections, the program ends
