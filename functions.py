'''
syntax func
def my_sum(a, b):     a,b are parameters and 2,3 are arguments                     
    return a + b
my_sum(2, 3)
'''
# def siri(we):
#     print("siri is a virtual assistant", we)
# siri("Hello")


# more than one parameter are called multiple parameter functions
'''

def add(a,b):
    print(a+b)
add(3,4)
add(100,1000000)
add(-2,5)'''

# while loop

# def add(a,b):
#     print(a+b)
# while True:
#     add(3,4)
    

# def siri(name):
#     print("hiii", name)
# n=input("enter your name: ")
# siri(n)

# # arbitary number of parameters
# def siri(*name):
#     print( name)
# siri("john","doe","alice")

# # keyworded arbitary number of parameters
# def siri(**name):
#     print(name)
# siri(name="satya",age=28)


# nested functions                            
# def out():
#     print("hello world")
#     def inn():
#         print("this is inner")
#     inn()
# out()


# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# add(5,3)
# sub(5,3)
# mul(5,3)


# def add(a,b):
#     return a+b
# c=add(5,3)
# print(c)'''





# # lambda functions
# '''
# def square(x):
#     f=lambda a:a*a
#     return f(x)
# input=int(input("enter the num"))
#print(square(input))




# def square(x):
#     a=lambda b:b*b
#     return a(x)
# out=int(input("enter the no.:"))
# print(square(out))



# f=lambda a,b:a*b
# c=f(3,2)
# print(c)



# l=[1,2,3,4,5]
# s=[]
# for i in l:
#     c=lambda a:a+1
#     s.append(c(i))
# print(s)
# '''


# # filter accepts true

# '''
# syntax 
# filter(function,sequence)

# age=[5,12,17,18,24,32]
# def func(x):
#     if x>=18:
#         return True
#     else:
#         return False
# adults=list(filter(func,age))
# print(adults)

# '''




# # map function
# '''
# syntax
# map(function,sequence)
# # filter true vunna data theeskuntadi no data change map anedi output lo change avthadi icchina inpuit ki

# def add(n):
#     return n+n
# numbers=(1,2,3,4)
# result=map(add,numbers)
# print(list(result))
# '''


# def add(x):
#     return x+x
# numbers=(1,2,3,4)
# result=map(add,numbers)
# print(list(result))

# def sub(x):
#     return x*x
# l=[1,2,3,4,5]
# result=map(sub,l)
# print(list(result))


# def even(s):
#     if s%2==0:
#         return "even"
#     else:
#         return "odd"
# numbers=[1,2,3,4,5,6,7,8,9,10]
# result=map(even,numbers)
# print(list(result))   
# '''                                                                          

# # reduce function
# # chala value ni oka single value ga convert chestadi
# '''
# from functools import reduce
# d=reduce(lambda a,b:a+b,[1,2,3,4,5])
# print(d)



# from functools import reduce
# d=reduce(lambda a,b:a*b,(9,2,8,9,8,9,8,9))
# print(d)
# '''

# # generator-function
# # idi nrml func lane untadi kaani return place lo yield use chestamu
# # return use cheste function oka sari run ayyaka exit avutadi kani yield use cheste function state ni save chesi next time call cheste akkada nunchi start avtadi
# ''''
# def mygen():
#     yield 1
#     yield 2
#     yield 3
# x=mygen()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# def mygen(a,b):
#     yield a+b
#     yield a*b
#     yield a-b
  
# x=mygen(5,10)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# from functools import reduce
# x=[1,2,3,4,5,6,7,8]
# def even(x):
#     if x%2==0:
#         print(x)
# result = list(map(lambda n: "even" if n % 2 == 0 else "odd", x))
# print(result)
# numbers=[1,2,3,4,5,6,7,8,9,10]
# map=list(map(lambda x: x*2,numbers))
# print(list(map))
# filter=list(filter(even,numbers))
# print(list(filter))



# def add(a,b):
#     return a-b
# print(add(2,4))

# def siri(x):
#     print(x+1)
# siri(9)




# task atm and calculator using functions'''


# # def cal():
# #     print("welcome to calculator")
# #     print("1.add")
#     # print("2.sub")
#     # print("3.div")
#     # print("4.mul")
#     # choice=input("enter the choice")
#     # num1=int(input("enter the  num"))
#     # num2=int(input("enter the  num"))
#     # if choice=="+":

#     #          print(num1 + num2)
#     # if choice=="-":
#     #          print(num1 - num2)
#     # if choice=="/":
#     #          print(num1 / num2)
#     # if choice=="*":
#     #          print(num1 * num2)
#     # else:
#     #     print("invalid")
# '''

# def atm():
#     pin=int(input("entetr your pin"))
#     if pin==pin:
#         print("1.withdraw")
#         print("2.deposit")
#         print("3.balance")
#         choice=input("enter your choice")
#         amount=10000
#         input_amount=int(input("enter the amount"))
#         if choice=="1":
           
#             if amount < input_amount:
#                 print("insufficient balance")
#             else:
#                 print(f"you have withdrawn {amount - input_amount}")
#         if choice=="2":
#             print(f"you have deposited {amount + input_amount}")
#         if choice=="3":
#             print(f"your balance is {amount}")
#     else:
#             print("invalid")
# atm()
#          '''


# def squ(a,b):
#     n=lambda a,b:a**b
#     return n(a,b)
# print(squ(2,3))


# l=[1,2,3,4,5,6,7,8,9,10]
# def sq(i):
#     if i*i>20:
#         return True
#     else:
#         return False
# result=list(filter(sq,l))
# print(result)


# n=lambda a: "positive" if a>0  else "negative" if a<0 else "zero"
# print(n(10))
# print(n(-5))
# print(n(0))
# print(chr(ord('A')))


# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x += 5
#         return x
#     return inner
# closure = outer()
# print(closure())



# def myfunc(a):
#     a = a + 2
#         a = a * 2
#     return a

# print(myfunc(2))

# print('cd'.partition('cd'))
# print('abef'.partition('cd'))
# print('abacji0ijb bjkj'.partition("ac"))

# def f(value, values):
#     v = 1
#     values[0] = 44
# a = 3
# v = [1, 2, 3]
# f(a, v)
# print(a, v[0])



# numbers = [3, 7, 2, 8, 5]
# for i, num in enumerate(numbers):
#    if i == num:
#        break
#    print(num, end=' ')

# def checkOddEven(x):
#     if x%2==0:
#         return "Even"
#     else:
#         return "Odd"
# x=int(input())
# print(checkOddEven(x))
# print(checkOddEven(4))
# print(checkOddEven(5))

 

# from collections import Counter 
 
# items = ['apple', 'banana', 'apple', 'orange', 'banana'] 
# count = Counter(items) 
# print(count) 

# def atm():
#     pin=int(input("entetr your pin"))
#     if pin==pin:
#         print("1.withdraw")
#         print("2.deposit")
#         print("3.balance")
#         choice=input("enter your choice")
#         amount=10000
#         input_amount=int(input("enter the amount"))
#         if choice=="1":
#            if amount < input_amount:
#                 print("insufficient balance")
#            else:
#                 print(f"you have withdrawn {amount - input_amount}")
#         if choice=="2":
#             print(f"you have deposited {amount + input_amount}")
#         if choice=="3":
#             print(f"your balance is {amount}")
#     else:
#             print("invalid")
# atm()


# l=[]
# l.append(("append",10))
# l.append(("append",20))
# l.append(("append",30))
# l.append(("insert",1,15))
# l.append(("remove",20))
# l.remove(("remove",20))
# l.remove(("append",20))






# print(l)

def manipulate_list(operations):
    lst = []  # start with an empty list

    for op in operations:
        if op[0] == "append":
            lst.append(op[1])

        elif op[0] == "insert":
            lst.insert(op[1], op[2])

        elif op[0] == "remove":
            lst.remove(op[1])

        elif op[0] == "pop":
            if lst:  # check to avoid popping from an empty list
                lst.pop()

    return lst


# Sample input
operations = [
    ("append", 10),
    ("append", 20),
    ("append", 30),
    ("insert", 1, 15),
    ("remove", 20)
]

# Function call
result = manipulate_list(operations)
print(result)  # Output: [10, 15, 30]






