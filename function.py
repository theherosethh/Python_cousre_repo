def greet():
    print("Hello world!")

greet()

def greet1(name, age=19):
    print("Hello", name ,age)

greet1("Seth")
# pass arguement

# greet("Seth")

# def sum(num1, num2):
#     sum = num1 + num2
#     print(f"The sum of num1 and num2 is {sum}")

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# sum(num1, num2)

# def sub(num1, num2):
#     sub = num1 - num2
#     print(f"The sub of num1 and num2 is {sub}")

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# sub(num1, num2)


# def mul(num1, num2):
#     multiple = num1 * num2
#     print(f"The sub of num1 and num2 is {multiple}")

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# mul(num1, num2)

# def div(num1, num2):
#     division = num1 / num2
#     print(f"The sub of num1 and num2 is {division}")

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# div(num1, num2)


# def calculation(num1, num2, operator):
#     match operator:
#         case "+":
#             print(num1 + num2)
#         case "-":
#             print(num1 - num2)
#         case "*":
#             print(num1 * num2)
#         case "/":
#             while (num2 == 0):
#                 print("cannot divided by zero")
#                 num2 = int(input("Enter num2 again: "))   
#             print(num1 / num2)
#         case _:
#             print("Invalid operator")

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# operator = input("Enter operator +,-,*,/ : ")

# calculation(num1, num2, operator)


#find_max
# def find_max(num1):
#     num2 = sorted(num1)
#     print(num2[-1])

# num = input("Enter number: ")
# num1 = list(map(int, num.strip().split()))
# find_max(num1)

#remove duplication
def remove_duplication(num1):
    remove = list(set(num1))
    return remove

# num = input("Enter number: ")
# num1 = list(map(int, num.strip().split()))
# remove1 = remove_duplication(num1)
# #print(remove1)

def reverse_string(str1):
    reverse = " ".join(str1[::-1])
    return reverse

# str = input("Enter string: ")
# str1 = list(str.split())
# reverse1 = reverse_string(str1)
# print(reverse1)