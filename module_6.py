# # --- Iterators and Generators in Python ---

# # A set (unordered collection of unique elements)
# s = {12, 34, 56, 78}

# # print(s[2]) # ❌ TypeError: 'set' object is not subscriptable because sets don't support indexing

# # Creating an iterator from the set
# s_iter = iter(s)  # iter() converts the set into an iterator object

# print(type(s_iter))  # <class 'set_iterator'> → confirms that s_iter is an iterator

# # Calling next() on the iterator gives one element at a time (order is random because sets are unordered)
# print(next(s_iter))  # returns first element from the set
# print(next(s_iter))  # returns next element
# print(next(s_iter))  # returns next element
# print(next(s_iter))  # returns next element
# # print(next(s_iter))  # ❌ StopIteration → raised when no more elements are left

# # Using a for loop to iterate through the set (Python automatically handles iter() and next())
# for i in s:
#     print(i)  # prints each element of the set

# # --- Iterators with Dictionary ---

# # Creating a dictionary
# d = {'a': 1, 'b': 2, 'c': 3}

# # Creating an iterator for the dictionary (iterates over keys by default)
# d_iter = iter(d)

# print(type(d_iter))  # <class 'dict_keyiterator'> → confirms it’s a dictionary key iterator

# # next() returns each key in the order of insertion
# print(next(d_iter))  # 'a'
# print(next(d_iter))  # 'b'
# print(next(d_iter))  # 'c'
# # print(next(d_iter))  # ❌ StopIteration → no more keys left

# # Iterating over dictionary using for loop
# for k in d:
#     print(k, d[k])  # prints each key and its corresponding value

# # --- Generator Function Example ---

# # Creating a list using list comprehension
# lst = [x for x in range(500)]  # list from 0 to 499

# # Defining a generator function that yields chunks of data
# def data_loader(chunk_size, lst):
#     # Loop from 0 to len(lst) in steps of chunk_size
#     for i in range(0, len(lst), chunk_size):
#         yield lst[i: i + chunk_size]  # yield returns one chunk and pauses the function

# # Creating a generator object
# x = data_loader(5, lst)

# print(type(x))  # <class 'generator'> → because of the 'yield' keyword
# print(x)        # prints memory address of generator object

# # Getting values from generator using next()
# print(next(x))  # returns first 5 elements [0, 1, 2, 3, 4]
# print(next(x))  # returns next 5 elements [5, 6, 7, 8, 9]

# # If you keep calling next(x), it will continue yielding 5-element chunks
# # until the list is exhausted, then raise StopIteration


# def square_addition(x,y):
#     return x**2 + y**2

# sq_add = lambda x,y: x**2 + y**2
# print(square_addition(3,4)) # 25

# # Normal function → uses return, gives one result, ends immediately.
# # Generator function → uses yield, gives one result at a time, pauses & resumes.
# # Lambda function → short one-line function, good for small tasks.
# # next() → used to get next value from a generator.
# # iter() → converts iterable into an iterator.
# # yield ≈ "return this value, but remember my position for next call."



# lst = [12,24,36,48,60]

# def square(x):
#     return x**2

# lst = list(map(square, lst))
# print(lst)






# #map
# string = "Hello this is Python programming"

# string1 = list(map(str.upper , string))
# print(string1)

# string1 = " ".join(string1)
# print(string1)

# #map with lambda
# lst = list(map(lambda x: x**2 if x%2 ==0 else x, lst))
# print(lst)


# using filter() and lambda to filter even numbers from an input list
# Input =  int(input("Input: "))
# lst = list(map(int, input().split()))
# even_numbers = list(filter(lambda x: x % 2 == 0, lst))
# print("Even Numbers:", even_numbers)

def safe_divide(a, b):
    try:
        result = a/b            
        print("Output: ",result)             
    except ZeroDivisionError:      
        print("Output: Division by zero") 
safe_devide(10,0)
