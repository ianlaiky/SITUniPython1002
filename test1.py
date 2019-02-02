def say(message, times = 2):
    print(message * times)

say('Hello')
say('World', 5)

def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c = 24)
func(c = 50, a = 100)

def func(a, b, names):
    a = a+10
    b = b+20
    names[0] = 12
    names[1] = 18
    return a,b

x,y=10,30

fruits= ['apple', 'orange', 'banana']

num1, num2=func(x,y,fruits)
print num1, num2
for fruit in fruits:
    print fruit