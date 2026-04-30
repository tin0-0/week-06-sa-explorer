# # # #test = int("h") #value error
# # # #file = open("missing.txt") #file not found error
# # # # d = {"a":1}
# # # # # print (d["b"]) #key error
# # # 1st = [1,2,3,10]
# # # print (1st[4]) #index error

# # try:
# #     age = int(input("Enter your age: "))
# #     print(f"In 10 years, you will be {age + 10} years old.")

# # except ValueError:
# #     print("This is not a valid number for age.")

# try:
#     filename = input("file to read:")
#     with open (filename) as f:
#         data= f.rad()
# except FileNotFoundError:
#     print(f"file '{filename}' not found.")
# except PermissionError:
#     print(f"You do not have permission to read '{filename}'.")
# else:
#     print(f"Read{len(data)} characters")
# finally:
#     print("Program finished.")

while True:
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Please enter a valid number for age.")
    else: 
        print(f"In 10 years, you will be {age + 10} years old.")    
        break