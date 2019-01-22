import sys

a = ""
try:
    a = str(sys.argv[1])

except:

    print "Your input is invalid!"

listt = str(a).split(",")
list = []
for i in listt:
    list.append(int(i))

# print list

sumOfEvenNumbers = 0
sumOfOddNumbers = 0
listEven = []
listOdd = []
for i in list:
    if int(i) % 2 == 0:
        listEven.append(int(i))
        sumOfEvenNumbers = sumOfEvenNumbers + int(i)
    else:
        listOdd.append(int(i))
        sumOfOddNumbers = sumOfOddNumbers + int(i)

differenceBetweenBigSmall = int(max(list)) - int(min(list))

sumall = int(sumOfEvenNumbers) + int(sumOfOddNumbers)
# print int(min(list))
minussumall = int(sumall)-(int(max(list))+int(min(list)))
# print minussumall
avg = minussumall/(len(list)-2)

print "The sum of all even numbers is " + str(sumOfEvenNumbers) + ", the sum of all odd numbers is " + str(
    sumOfOddNumbers) + ", the difference between the biggest and smallest number is " + str(differenceBetweenBigSmall) + ",the total number of even numbers is " + str(
    str(len(listEven))) + ", the total number of odd numbers is " + str(len(listOdd))+", the centered average is "+str(avg)
