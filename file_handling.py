# file = open('example.txt', 'w')
# file.write('hello omi this is your txt file')
# file.close()

# file = open('example.txt', 'r')
# show = file.read()
# print(show)
# file.close()


# file = open('example.txt', 'r')
# a = file.read()
# show = file.readline()
# print(show)
# print(a)
# file.close()

# file = open('example.txt', 'a')
# file.write('of couurse')
# file.close()

#Remaining file handling operations
# import os
# os.rename('example.txt', 'new_example.txt')

# Deleting a file
# import os
# os.remove('example22.txt')

# File Mode (r+, w+, a+)
# r+ Mode
# file = open('new_example.txt', 'r+')
# file.write('omi')
# file.seek(0)
# print(file.read(4))
# file.close()

#w Mode
file = open('new_example.txt', 'w+')
file.write('omisss')
file.seek(0)
print(file.read(3))
file.close()
