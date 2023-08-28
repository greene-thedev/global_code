# Definig the function
def is_even(number):
	return number % 2 == 0


# defining iterable
numbers = [1,56,234,87,4,76,24,69,90,135]


# returning even numbers in the iterable
for number in numbers:
	if is_even(number):
		print(number)

print('********using lambda************')

# rewriting the above code using lambda

# defining the lambda function
is_even = lambda x: x % 2 == 0

# returning even numbers in the iterable
for x in numbers:
	if is_even(x):
		print(x)

print('********using not*********')

# returning odd numbers in the iterable using not
for x in numbers:
	if not is_even(x):
		print(x)
