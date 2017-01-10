a = raw_input("give me a word: ")
x = len(a)
if len(a) % 2 == 0:
    if a[0:x/2] == a[x/2:x][::-1]:
        print "IT IS PALINDROME"
    else:
        print "and.... you fail"
else:
    if a[0:x/2] == a[x/2+1:x][::-1]:
        print "IT IS PALINDROME"
    else:
        print "and.... you fail"
