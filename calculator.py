import sys

error = False
avg = float(0.0)

a = 0.0
b = 0.0
c = 0.0
try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except ValueError:
    error = True
    print "Your input is invalid"

if not error:
    avg = (float(a) + b + c) / 3

    print avg
