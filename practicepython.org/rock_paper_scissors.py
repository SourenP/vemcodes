c = "yes"
while (c == "yes"):
    print "1 = rock 2 = paper 3 = scissors: "
    a = int(raw_input("give me a number 1-3: "))
    b = int(raw_input("give me a number 1-3: "))
    if a == 1 and b == 3:
        print "Congratulations the picker of rock!"
    elif a == 1 and b == 2:
        print "Congratulations the picker of paper!"
    elif a == 2 and b == 3:
        print "Congratulations the picker of scissors!"
    elif a == 2 and b == 1:
        print "Congratulations the picker of paper!"
    elif a == 3 and b == 1:
        print "Congratulations the picker of rock!"
    elif a == 3 and b == 2:
        print "Congratulations the picker of scissors!"
    elif a == 1 and b == 1 or a == 2 and b == 2 or a == 3 and b == 3:
        print "Tie"
    else:
        print "next time please pick from the numbers 1-3 thanks you"
    c = raw_input("do you want to start a new game (yes/no)? ")
