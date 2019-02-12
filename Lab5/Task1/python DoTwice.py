import sys


def double(x):
    return 2*x

def square(x):
    return x**2

def cube(x):
    return x**3
def doTwice(x,y):
    return x(x(y))


b = int(sys.argv[1])
a = int(sys.argv[2])

listy = [double,square,cube]

try:
    print doTwice(listy[int(a)-1],int(b))
except:
    print "It cannot be supported!"

