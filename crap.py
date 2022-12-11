# try:
#     a=int(input("a: "))
#     b=int(input("b: "))
#     c=a+b
#     e=a/b
#     print("try successful")
# except ArithmeticError:
#     print("arithemetic error occured")
# except Exception:
#     print("exception occured")
# else:
#     print("hi")
# finally:
#     print("executed in any condition")
# marks={"kusmus": 30, "husmus": 40, "busmus": 77}
# name= input()

# try:
#     print("marks:",marks[name])
# except KeyError:
#     print("name {} not in the list".format(name))
# print("end of program")
# try:
#     fh= open("testfile","r")
#     fh.write("This is my test file for exception handling!!")
# except IOError:
#     print("Error: can't find file or read data")
# else:
#     print("Content written succesfully")
def checkage(age):
    if age<0:
        raise ValueError ("age should be greater than or equal to zero")
    print("age is valid")
try:
    age=int(input("age: "))
    checkage(age)
except ValueError as err:
    print(err.args)
finally:
    print("executed in any condition")