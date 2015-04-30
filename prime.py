def is_prime(x):
    x = int(x)
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2, x):
            # print "Remainder for %d is %d" % (n, x % n)
            if x % n == 0:
                return False
        return True
while True:
    number = raw_input("Number to test: ")
    print is_prime(number)