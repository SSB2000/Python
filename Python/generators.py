# Generators
'''
Generator don't store/hold entire result in memory like list/array, it YIELDS 1 result at a time
'''

import sys

# Array

my_nums = [x * x for x in [1, 2, 3, 4, 5]]
print(my_nums)
print(sys.getsizeof(my_nums))

# same thing via generator
def square_numbers(nums):
    for i in nums:
        yield(i * i)
    
my_nums = square_numbers([1, 2, 3, 4, 5])

print(next(my_nums))
print(next(my_nums))
print(sys.getsizeof(next(my_nums)))

for num in my_nums:
    print(num)

# Output
'''
[1, 4, 9, 16, 25]
120
1
4
28
16
25
'''

# list = [] generator = ()

# Ref: Corey Schafer's Python Tutorial: Generators - How to use them and the benefits you receive: https://www.youtube.com/watch?v=bD05uGo_sVI