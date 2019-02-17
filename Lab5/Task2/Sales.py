import sys


def scale(listy,x):
    return [i * x for i in listy]

# print scale([30,40,50],0.1)


def lastchar(x):
    # print str(x)[-1]
    return str(x)[-1]

def sort(list1):
    return sorted(list1, key=lastchar)


def goodSales(listy):
    returninglist = []
    total = 0
    for i in listy:
        total = total + int(i)
    avg = int(total)/len(listy)

    for i in listy:
        if int(i)> int(avg):
            returninglist.append(int(i))
    return returninglist

a = str(sys.argv[1])
b = str(sys.argv[2])

# print map(int,a.split(","))

print "The scaled number is: "+str(scale(map(int,a.split(",")),int(b))) +" The sorted sales numbers are: "+ str(sort(map(int,a.split(","))))+" The good sales numbers are: "+str(goodSales(map(int,a.split(","))))