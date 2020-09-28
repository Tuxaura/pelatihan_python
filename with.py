# file handling
# tanpa with statement
file = open('file_dir', 'w')
file.write('hello world')
file.close()

file = open('file_dir', 'w')
try:
    file.write('hello world')
finally:
    file.close

# dengan menggunakan with statement
with open('file_dir', 'w') as file:
    file.write('hello world')
