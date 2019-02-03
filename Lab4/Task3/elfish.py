def elfish(x):

    if str(x) == "":
        return x

    else:
        # print x
        if x[0] == "e":
            return elfish(x[1:])+x[0]
        if x[0] == "l":
            return elfish(x[1:])+x[0]
        if x[0] == "f":
            return elfish(x[1:])+x[0]
        else:
            return elfish(x[1:])

print elfish("walesff")