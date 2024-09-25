#python function
#arbitrary argument in python
# def my_function(name):
#     print("hello " + name)

# my_function("ray")

# def myfunction(*kids):
#     print("the young child is " + kids[2])

# myfunction("emil","tobias","linux")

# def my_function(child3, child2, child1):
#     print("the youngest child is " + child3)

# my_function(child1="ray", child2= "faith", child3= "success")

# def my_function(country="Norway")
    
#     print("i am from "+ country)

# my_function("seadon")

# my_function("india")

# my_function()

# my_function

# def my_function1():
#     pass
# recursion it means python can call itself
#be very careful cause it can leaad into infinite loop

# def tri_recursion(k):
#     if(k>0):
#         result = k + tri_recursion( k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

    

# print("\n\n Recursion Example Results")

# tri_recursion(6)

#lambda function

x = lambda a : a +10
print(x(5))

#lambda can take two argument

x = lambda a, b : a+b

print(x(5,6))

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)

print(mydoubler(11))

