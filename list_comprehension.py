# Syntax list comprehension
#  [expression for item in list]

y = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
