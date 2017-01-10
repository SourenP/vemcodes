number = int(raw_input("give me a number and ill tell you if its prime or not: "))
a = 1
while a < number - 1:
    a = a + 1
    if number % a  == 0:
        print "your number is not prime"
    else:
        print "your number is prime"

    print a
