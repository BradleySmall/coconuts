def splitthem(quant):
    if quant[0] % 5 != 1:
        return False
    else:
        quant[0] -= (1 + quant[0]//5) 
    return True


def testnum(num):
    for pers in range(5):
        if (False == splitthem(num)):
            return False
    if num[0] % 5 == 0:
        return True


def main():
    num = [0]
    for n in range(1, 10000):
        num[0] = n
        if testnum(num):
            print "The Number Was %d" % (n)
            return

    print "Not found in 10000 tries"


if __name__=="__main__":
    main()
