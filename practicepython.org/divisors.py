a = int(raw_input("give me a number and TADAA i gave you all the devisors: "))
for i in range(1,a+1):
    if a % i == 0:
        print i
    else:
        pass
