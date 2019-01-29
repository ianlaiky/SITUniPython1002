import sys

from myMath import *


a = ""
try:
    a = str(sys.argv[1])

except:

    print "Your input is invalid!"

noList = a.split(",")

newList = []
# print noList

for i in noList:

    newList.append(int(i))

print "The difference is:" + str(subtraction(maximum(newList), minumum(newList))) +" The summation is:"+str(add(maximum(newList), minumum(newList))) +" The summation of all input is:" + str(
    sumTotal(newList)) + " The number of even numbers is:" + str(evenNumber(newList)) + " The values in the list are: "+str(clear(newList))