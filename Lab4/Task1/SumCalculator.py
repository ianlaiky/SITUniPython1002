import sys

a = int(sys.argv[1])
def sum_recursive(x):
    if x == 0:
        return x
    else:
        return sum_recursive(x-1)+x

def sum_iterative(x):
    out = 0
    for i in range(x):
        out += i+1

    return out

print "The SUM value calculated by recursive is "+str(sum_recursive(a))+" and by iterative is "+str(sum_iterative(a)) +"."