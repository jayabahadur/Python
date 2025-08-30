def number_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
 
numbers = number_generator()
print(next(numbers))