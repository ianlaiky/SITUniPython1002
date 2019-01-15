import sys

a = 0.0
b = 0.0
c = 0.0

error = False

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except:
    print "Your input is invalid!"

workingHour = float(a)
normalHour = float(a)
overtimeHour = 0
normalRate = float(b)
overTimeRate = float(c)

if not error:
    if workingHour < (7 * 24):
        if workingHour > float(40.0):
            overtimeHour = workingHour - float(40.0)
            normalHour = 40.0
        normalPay = normalHour * normalRate
        overtimePay = overtimeHour * overTimeRate
        totalPay = normalPay + overtimePay

        print "Normal Salary:%.2f" % normalPay
        print "Extra Salary:%.2f" % overtimePay
        print "Total Salary:%.2f" % totalPay
    print "Your input is invalid!"
