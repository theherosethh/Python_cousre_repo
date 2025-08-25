#comparison operator
 
# > greater than , < less than , == equal to ,
# >= greater than or equal to , <= less than or equal to
#it only reture true or false
#example

# x = 5
# y = 3

# print(x > y)


#logical operator

# there are three clause in logical operator 
#(and), (or), (not)
#(and) reture true if both statements are true, if one is true the return is false
#example of (and)

# x = 5
# y = 2

# print(x > 2 and x < 6)

#(or) reture true if one of the two statement is true

#example

# print(x > 2 or x < 3)

#(not) reverse the reture of the statement if x is true then (not) reverse to false

#example

# print(not(x < 2))

#Exercise

age = int(input("How old are you?: "))

if age >= 13 and age >= 19:
    print("You are a teenager")
else: print("you are not a teenager")