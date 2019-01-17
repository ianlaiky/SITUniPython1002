import sys

try:
    a = str(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except:
    print "Your input is invalid!"
if (float(b) >0.0 and float(c)>0.0):
    if (str(a).lower() == "metric".lower()) or (str(a).lower() == "imperial".lower()):
        height = float(b)
        weight = float(c)
        bmi = 0.0
        if str(a).lower() == "metric".lower():
            bmi = weight / height ** 2
        if str(a).lower() == "imperial".lower():
            bmi = 703 * weight / height ** 2

        bmi = "%.2f" % bmi
        cat = ""
        if float(bmi) < float(16):
            cat = "Severe Thinness"
        elif float(bmi) >=float(17) and float(bmi) <=float(17):
            cat = "Moderate Thinness"
        elif float(bmi) >=float(17) and float(bmi) <= float(18.5):
            cat = "Mild Thinness"
        elif float(bmi) >=float(18.5) and float(bmi) <=float(25):
            cat = "Normal"
        elif float(bmi) >=float(25) and float(bmi) <= float(30):
            cat = "Overweight"
        elif float(bmi) >=float(30) and float(bmi) <=float(35):
            cat = "Obese Class I"
        elif float(bmi) >=float(35) and float(bmi) <=float(40):
            cat = "Obese Class II"
        elif float(bmi) > float(40):
            cat = "Obese Class III"

        print str(bmi) + " " + cat
    else:
        print "Your input is invalid!"
else:
    print "Your input is invalid!"
