## Concepts:
    ## map
    ## lambda
    ## filter


# items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# cubes = list(map(lambda x: x**3, items))  # Corrected placement of parentheses
# print(cubes)


## defining a function to detect old people:
def too_old(x): return x > 30
# print(too_old(23))


## filtering a list according to too_old in a list form:
ages = [22, 25, 29, 34, 56, 24, 12]

# print(list(filter(too_old,ages)))
## returning the length of the above:
print(len(list(filter(too_old,ages))))