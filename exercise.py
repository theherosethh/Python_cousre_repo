# input = (input("Input a string: "))
# input1 = input[::-1]
# print(input1)

#count vowel
# input = (input("Input a string: "))
# vowels = 0
# consonants = 0 

# for i in input:
#     if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
#        or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
#         vowels = vowels + 1
#     else:
#         consonants = consonants + 1
 
# print("Total Number of Vowels in this String = ", vowels)
# print("Total Number of Consonants in this String = ", consonants)


# str1 = input("Please input: ")
# vowel_dict = "aeiou"
# vowel = 0 
# constand = 0
# for char in str1:
#     if char.isalpha:
#         if char.lower() in vowel_dict:
#              vowel += 1
#     else:
#         constand += 1


# input1 = input("word: ")
# input1 = input1.lower()
# if input1 == input1[::-1]:
#     print(f"{input1} is a palindrome")
# else:
#     print(f"{input1} isn't a palindrome")


#take input
#loop through each word and compare
#print the longest word


# s = input("word: ")
# words = s.split()

# longest = ""

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print(f"{longest} is the longest.")

# s = input("word: ")
# words = s.split()
# join = "_".join(words)
# print(join)



# Input = [1, 2, 3, 4, 5]
# sum1 = sum(Input)
# print(sum1)


# number = []
# for i in range (5):
#     num = int(input(f"Enter number {i+1}: "))
#     number.append(num)
# print(f"You have input {number}")
# sum1 = sum(number)
# print(f"The sum of your input are:  {sum1}")

# num = input("Input 1-5 : ")
# answer = list(map(int, num.strip().split(" ")))

# print(answer)

# print(sum(answer))

# num = input("Input 1-5 numbers: ")
# split1 = num.split()
# nun_max = max(split1)
# num_min = min(split1)

# print(f"Max = {nun_max}, Min = {num_min} ")

# num = input("Enter number: ")
# num1 = list(map(int, num.strip().split()))

# remove_duplicat = list(set(num1))
# print(remove_duplicat)

#count occourance
# num = input("Enter numbers separated by spaces: ")
# num1 = list(map(int, num.strip().split()))

# value = int(input("Enter value to count: "))

# count = num1.count(value)

# print(count)

#merge list

# num1 = input("Enter numbers of list 1: ")
# num2 = list(map(int, num1.strip().split()))
# print(num2)
# num3 = input("Enter numbers of list 2: ")
# num4 = list(map(int, num3.strip().split()))
# print(num4)

# num2.extend(num4)
# print(num2)

#find seccond largest 
# num = input("Enter numbers: ")
# num1 = list(map(int, num.strip().split()))

# largest = max(num1)

# while largest in num1:
#     num1.remove(largest)

# if num1:
#     second = max(num1)
#     print("The second largest number is:", second)
# else:
#     print("There is no second largest number.")


#return new list with common element:
# from collections import Counter
# num1 = input("Enter numbers of list 1: ")
# num2 = list(map(int, num1.strip().split()))
# c1 = Counter(num2)
# print(num2)
# num3 = input("Enter numbers of list 2: ")
# num4 = list(map(int, num3.strip().split()))
# c2 = Counter(num4)
# print(num4)

# common = list((c1 & c2).elements())
# print(f" common from list {common}")

#remove all element appear more than one
from collections import Counter
num = input("Enter numbers: ")
num2 = list(map(int, num.strip().split()))

count = Counter(num2)

duplicate = [item for item in num2 if count[item] == 1]
print(duplicate)