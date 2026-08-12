#Exception Handling


try:
    result = 2/0
except ZeroDivisionError:
    print("please check your calculation it maybe did not currect")

finally:
    result = 1
print(result)