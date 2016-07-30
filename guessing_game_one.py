import random
a = random.randint(1, 9)
b = int(raw_input("guess the number YOU IMBECILE btw its 1-9: "))
if a == b:
    print "WTF man howd you do that YOU GUESSED IT CORRECT"
elif b < a:
    print "ya i thought so you were wrong its a bit bigger"
elif b > a:
    print "ya i thought so you were wrong its a bit smaller"
elif b < 1 or b > 9:
    print "do you know what guess the number YOU IMBECILE btw its 1-9 means?"
else:
    print "ya please dont put words"
