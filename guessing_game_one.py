

b = 3425245
import random
a = random.randint(1, 9)
while(a != b):
    b = raw_input("guess the number YOU IMBECILE btw its 1-9 or you can just type exit and the game will stop: ")
    if b == "exit":
        break
    else:
        b = int(b)
    if a == b:
        print "WTF man howd you do that YOU GUESSED IT CORRECT"
    elif b < a:
        print "ya i thought so you were wrong its a bit bigger"
    elif b > a:
        print "ya i thought so you were wrong its a bit smaller"
    elif b < 1 or b > 9:
        print "do you know what guess the number YOU IMBECILE btw its 1-9 means?"
    else:
        print "uhhhhhh just enter the numbers or break"
