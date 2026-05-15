# firstname=input("pls inter your first name")     
# scondname=input("pls inter your scond name") 
# name=firstname+" "+scondname
# print("my name is"+name)  


# fruits=['apple','bannana','cherry'] 
# print(fruits) 
# print("start use append to add orange") 
# fruits.append("orange") 
# print(fruits) 

# print("start use copy ")
# x=fruits.copy() 
# print(x) 

# print("start use count") 
# a=fruits.count("cherry") 
# print(a) 

# cars=['ford','bmw','volvo'] 
# print("start use extend cars+fruits")
# fruits.extend(cars) 
# print(fruits) 

# print("start use index") 
# z=fruits.index("apple") 
# print(z) 

# print("start use isert") 
# fruits.insert(0, "watermelon") 
# print(fruits)  

# print("start use pop to delete index 1") 
# fruits.pop(1) 
# print(fruits)

  
# print("start use reverse") 
# rfruits=fruits 
# rfruits.reverse() 
# print(fruits) 


# print("start use clear") 
# fruits.clear() 
# print(fruits)  


# print("start use sort") 
# carsSorted=cars 
# carsSorted.sort
# print(carsSorted) 


# fruits = ["apple", "orange", "banana"]
# for x in fruits:
#     print(x)
 

# def my_function(): 
#  print("hello from function") 
# my_function 
# def my_functoin(name):
#     print("hello",name)  


# students = ["yarob", "omar", "khaled"]

# def getStudents(lst):
#     for student in lst:
#         if student == "omar":
#             print(student + " is there")

# getStudents(students)




# مشروع العملي الخاص بكود الآلة الحاسبة - الصف الثاني متوسط /2


# Simple calculator program

# # Get numbers from user
# num1 = float(input("Enter the first number: "))
# operator = input("Choose operation (+, -, *, /): ")
# num2 = float(input("Enter the second number: "))

# # Perform calculation based on the operator
# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Cannot divide by zero!"
# else:
#     result = "Invalid operation"

# # Display the result
# print("Result:", result)   






# بناء كود يقوم بحساب العمر  

# from datetime import datetime

# # Ask the user for birth date
# birth_date = input("Enter your birth date (example: 2012/8/6): ")

# # Convert the string to a datetime object
# birth_date = datetime.strptime(birth_date, "%Y/%m/%d")

# # Get current time
# now = datetime.now()

# # Calculate difference
# difference = now - birth_date

# # Calculate years accurately
# years = now.year - birth_date.year
# if (now.month, now.day) < (birth_date.month, birth_date.day):
#     years -= 1

# # Days from difference
# days = difference.days

# # Time parts
# hours = difference.seconds // 3600
# minutes = (difference.seconds % 3600) // 60
# seconds = difference.seconds % 60

# # Print results
# print("Your age:")
# print("Years:", years)
# print("Total Days:", days)
# print("Hours:", hours)
# print("Minutes:", minutes)
# print("Seconds:", seconds)




# بناء الة حاسبة بطريقة اخرى 



# num1=int(input("enter your first number:")) 
# p=input() 
# num2=int(input("enter your second number")) 
# def g(x, y):
#     return x+y 
# def t(x,y): 
#     return x-y 
# def d(x,y):
#     return x*y 
# def q(x,y): 
#     return x/y
# if p=="+": 
#   print(g(num1,num2)) 
# elif p=="-": 
#   print(t(num1,num2)) 
# elif p=="*": 
#   print(d(num1,num2)) 
# elif p=="/": 
#   print(q(num1,num2))
