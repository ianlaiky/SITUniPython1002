import sys
from collections import Counter

a = ""
try:
    a = str(sys.argv[1])

except:

    print "Your input is invalid!"

word = Counter(str(a).lower())
count = 0
wordlist = ""

for oiw in sorted(word, key=word.get, reverse=True):
    count = count + 1
    wordlist = str(wordlist) + "," + oiw + ":" + str(word[oiw])
    if count == 5:
        break
print wordlist[1:]
