import sys

a = int(sys.argv[1])
def digit(x):
    if x < 10:
        return 1
    else:
        return digit(x // 10) + 1


def digit_iterative(x):
    count = 1

    while x > 10:
        x = x // 10
        count += 1
    return count


print "The number of digit(s) calculated by recursive is "+str(digit(a))+" and by iterative is "+ str(digit_iterative(a)) +"."
