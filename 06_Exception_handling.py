# a = int(input("please tell your number:- "))

# try:
#     print(10/a)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# print("i have done the division")

# koi bhi error ko define kr dega yeh code 
# a = int(input("please tell your number:- "))
# try:
#     print(10/a)
# except Exception as e:
#     print(f"Error: {e}")

# print("i have done the division")


# agar except block run nhi hoga that means ki else block execute ho jayega 

# a = int(input("please tell your number:- "))
# try:
#     print(10/a)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# else:
#     print("Division was successful.")

# print("i have done the division")



# finally block will always execute whether there is an error or not
# try:
#     print(10/a)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# else:
#     print("Division was successful.")
# finally:
#     print("This block always executes.")

# print("i have done the division")



# raise means ki hum manully throw kr skte he exception

# age = int(input("tell your age :- "))
# try:
#     if age < 10 or age > 18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")
# except Exception as err:
#     print(f"an error occured as {err}")

# print("the club will start soon")