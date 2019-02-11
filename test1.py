# def say(message, times = 2):
#     print(message * times)
#
# say('Hello')
# say('World', 5)
#
# def func(a, b=5, c=10):
#     print('a is', a, 'and b is', b, 'and c is', c)
#
# func(3, 7)
# func(25, c = 24)
# func(c = 50, a = 100)
#
# def func(a, b, names):
#     a = a+10
#     b = b+20
#     names[0] = 12
#     names[1] = 18
#     return a,b
#
# x,y=10,30
#
# fruits= ['apple', 'orange', 'banana']
#
# num1, num2=func(x,y,fruits)
# print num1, num2
# for fruit in fruits:
#     print fruit


# def reverse(stri):
#     if stri =="":
#         return stri
#     else:
#         return reverse(stri[1:])+stri[0]
#
# print reverse("gniknissidlrowehtolleh")

#
# def printMax(a, b):
#     if a > b:
#         print (a, 'is maximum')
#     elif a == b:
#         print a, 'is equal to', b
#     else:
#         print b, 'is maximum'
#
#
# printMax('charlie', 'chllo')

# def func(a, b=5, c=10):
#     print('a is', a, 'and b is', b, 'and c is', c)
# 
# func(3, 7)
# func(25, c = 24)
# func(c = 50, a = 100)

# def func(a, b, names):
#     a = a+10
#     b = b+20
#     names[0] = 12
#     names[1] = 18
#     return a,b
# x,y=10,30
# fruits=['apple', 'orange', 'banana']
# num1, num2=func(x,y,fruits)
# print num1, num2
# for fruit in fruits:
#     print fruit


# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return fact(n-1)*n
#
# print fact(4)
#
# x = 1
#
# for i in range(1,5):
#
#     x = int(x) * int(i)
#
# print x


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print fib(5)
