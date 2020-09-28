items = [
    ("Odol", 2500),
    ("sabun", 8000),
    ("kecap", 3000),
]
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)
# numbers = [2, 1, 4, 8]
# numbers.sort(reverse=True)
# print(sorted(numbers))
# print(numbers)
