## loops intro

# i = 0
# while(i < 10):
#     i = i + 1
#     print(i)




## Print numbers from 7 to 19

# i = 7
# while(i<20):
#     print(i)
#     i = i + 1




## Print even numbers between 12 and 20

# i = 12
# while(i<20):
#     print(i)
#     i = i + 2




## Write a function called evens that takes two numbers and prints all the even numners between them.

# def evens():
#     pointer = int(input('enter your lower limit: '))
#     limit = int(input('enter your upper limit(don\'t go crazy): '))

    
#     while(pointer < limit):
#         if(pointer%2 == 0):
#             print(pointer)
#         pointer += 1

#     return 'Good stuff!'

# evens()




## Write a function that returns the reverse of inputed values

# def reverse_evens():
#     pointer = int(input('enter your lower limit: '))
#     limit = int(input('enter your upper limit(don\'t go crazy): '))

#     while(limit > pointer):
#         if(limit%2 == 0):
#             print(limit)
#         limit -= 1

#     return 'Good stuff!'

# reverse_evens()



# While loop trial:

# for i in range(1,11):
#     print(i)

# for j in [1, 2, 3]:
#     print(j)



# Lists





# list = []
# list.append('a')
# list.append('b')
# list.append('c')
# list.append('d')
# list.append('e')
# list.pop()

# print(type(list))



## Write a function that takes two args(min and max) and returns a list of even numbers between them

# def create_list(min, max):
#     even_numbers = []
    
#     for i in range(min,max+1):
#         if(i%2==0):
#             even_numbers.append(i)   
        
#     return even_numbers

# print(create_list(1,19))



## Write a function produce the following output: 

# def asterics():
#     for i in range(1,5):
#         print('****')

#     return 'well done'    

# print (asterics())


## Write a function produce the the followint output:
# *
# **
# ***
# ****
# ***
# **
# *

# def incremental_asterics():
#     for i in range(1, 5, 1):
#         print('*'*i)
#     for i in range(3, 0, -1):
#         print('*'*i)  
    

#     return 'well done'

# print(incremental_asterics())



## Write a function that asks a user for his year of birth and calculates their age accordingly

# import datetime

# def age():
#     dob = int(input('Enter your year of birth: '))
#     current_year = datetime.date.today().year
#     age = current_year - dob
#     print(age)

#     return 'done'

# print(age())



# # Write a function that takes inputs from a user and populates a dictionary.

# def populate():
#     people = {}
#     username = "test"

#     while (username != "q"):
#         username = input('Enter username: ')
#         if (username == "q"):
#             break
#         age = int(input('Enter age: '))
#         people[username] = age

#     print(people)

# print(populate())