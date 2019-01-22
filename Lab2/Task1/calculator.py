import sys

leapYr = 2001

a = float(sys.argv[1])
b = float(sys.argv[2])



listLeap = []
for xy in range(int(a),int(b)+1):
    print xy
    if int(xy) % 4 == 0:

        if int(xy) % 100 != 0:

            listLeap.append(xy)
        elif int(xy) % 400 == 0:
            listLeap.append(xy)


leapyrstring = ""

for i in listLeap:
    leapyrstring=leapyrstring+str(i)+", "

print "The number of Leap Years is "+str(len(listLeap))+", the Leap Years are "+str(leapyrstring[:-2])

