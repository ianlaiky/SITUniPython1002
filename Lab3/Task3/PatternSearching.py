import sys

a = ""
b = ""
try:
    a = str(sys.argv[1])
    b = str(sys.argv[2])

except:

    print "Your input is invalid!"
count = 0

for index in range(len(a)):
    '''
    Counting from the first index to the current index + length of b
    '''
    if str(b) in str(a[index:int(index) + len(b)]):
        count += 1
print "Pattern appears " + str(count) + " time!"
