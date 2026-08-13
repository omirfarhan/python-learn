# #Directory handling
# import os
# os.mkdir('New Folder')

# #create file in directory
# file = open('New Folder/example.txt', 'w')
# file.write('hello omi this is your txt file its new create file in new folder')
# file.close()

# #Read File in directory

# file = open('New Folder/example.txt', 'r')
# show =file.read()
# print(show)
# file.close()

# # File in folder in folder
# import os
# os.makedirs('New Folder/New Folder 2', exist_ok=True)
# file = open('New Folder/New Folder 2/Example.txt', 'w')
# file.write('hello omi this is your txt file its new create file in new folder')
# file.close()

# #Rename File
# import os
# os.rename('New Folder/New Folder 2', 'New Folder/Test Folder')

#Delete file
import os 
os.remove('New Folder/Test Folder/Example.txt')