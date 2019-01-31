import sys
from collections import Counter

a = ""
try:
    a = str(sys.argv[1])
except:
    print "Your input is invalid!"
def letter_count(x):
    return dict(Counter(x))
def double_count(x, y):
    dixtx = dict(Counter(x)+Counter(y))
    return dixtx
def various_count(*strr):
    l = ""
    for i in list(strr):
        l=l+str(i)
    return Counter(l)
a = ""
try:
    a = str(sys.argv[1])
except:
    print "Your input is invalid!"
word = str(a).replace(",","")

dic = dict(Counter(word))
pr = ""
for i in sorted(dict(dic),reverse=True):
    pr=str(pr)+str(i)+":"+str(dic[i])+" "
print pr