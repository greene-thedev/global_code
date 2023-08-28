from functools import fold

# defining function
def join_strings(x, y):
	return x + y

#print(join_strings("hello", "hi"))

# defining iterable
words = ['jeremiah ', 'greene ', 'ackon ']

#joining words using fold

print(fold(join_strings, words))


