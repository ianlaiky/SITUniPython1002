import sys
from collections import Counter

a = ""
try:
    a = str(sys.argv[1])

except:

    print "Your input is invalid!"


def letter_count(x):
    return dict(Counter(x))


print letter_count("Thisit")


def double_count(x, y):
    dixtx = dict(Counter(x)+Counter(y))
    # print dixtx





# print dict(letter_count("Thisisit"))

double_count("This", "isit")
