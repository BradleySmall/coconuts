def splitthem(quant):
    """
    take a quantity and return False if it is not one more than 
    equally divisible by 5

    Otherwise, subtract 1 and subtract 1/5 of the remaining
    """
    if quant[0] % 5 != 1:
        return False
    else:
        quant[0] -= (1 + quant[0]//5) 
    return True


def testnum(num):
    """
    for a given number test to see if it will succeed using the 
    logic for split defined in splitthem 5 times.

    Then test to see that it is equally divisible by 5


    """
    for pers in range(5):
        if not splitthem(num):
            return False

    if num[0] % 5 == 0:
        return True
    else:
        return False


def main():
    """
    Main driver for the brute force solver

    choose a number and see if the result can be found and return 
    or print an error

    """
    TESTQUANTITY = 1000000

    num = [0]
    for n in range(1, TESTQUANTITY):
        num[0] = n
        if testnum(num):
            print ("The Number Was %d" % n)
            return

    print ("Not found in %d tries." % TESTQUANTITY)


if __name__=="__main__":
    main()