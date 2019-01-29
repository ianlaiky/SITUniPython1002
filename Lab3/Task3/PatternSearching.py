import sys

a = ""
b = ""
try:
    a = str(sys.argv[1])
    b = str(sys.argv[2])

except:

    print "Your input is invalid!"

res = 0
count = 0
while int(res) != -1:
    if b in a:
        index = a.index(b)
        lee = len(b)
        a = a[:0] + a[lee + index:]
        count += 1
    else:
        res = -1

print "Pattern appears " + str(count) + " time!"
