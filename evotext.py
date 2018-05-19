#!/usr/bin/env python
import string, random, time, sys
possibleChars = string.ascii_letters + string.digits + string.punctuation + " "
tries = 0
if len(sys.argv) > 1:
    target = " ".join(sys.argv[1:])
else:
    target = raw_input("Enter text here: \n")
attemptThis = ''.join(random.choice(possibleChars) for i in range(len(target)))
completed = False
while completed == False:
    sys.stdout.write('\r' + attemptThis)
    sys.stdout.flush()
    attemptNext = ""
    completed = True
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(possibleChars)
        else:
            attemptNext += target[i]
    attemptThis = attemptNext
    tries += 1
    time.sleep(0.02)
print("")
print("Took " + str(tries) + " tries")
