import random
z = 0
while z < 10:
    a = []
    b = []
    a.append(random.randint(0, 100))
    b.append(random.randint(0, 100))
    c = [i for i in a if i in b and i not in c]
    z = z + 1


    print c



print "you are going to run the proggram 10 times cuz numbers match in this 10% of the time"
