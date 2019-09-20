#!/usr/bin/python3

def splitthem(quant, running_count):
    """
    take a quantity and return False if it is not one more than 
    equally divisible by 5

    Otherwise, subtract 1 and subtract 1/5 of the remaining
    
    when the split is done, update the running count for whichever
    first zero value
    """
    if quant[0] % 5 != 1:
        return False
    else:
        share_amt = (quant[0]-1)//5
        for k in range(5):
            if running_count[k] == 0:
                running_count[k] = share_amt
                break
        quant[0] -= (1 + share_amt) 
    return True


def testnum(num, running_count):
    """
    for a given number test to see if it will succeed using the 
    logic for split defined in splitthem 5 times.

    Then test to see that it is equally divisible by 5

    When successful the running_count will be updated
    one last time for the final split.
    """
    for pers in range(5):
        if not splitthem(num, running_count):
            return False

    if num[0] % 5 == 0:
        share_amt = num[0]//5
        for i in range(5):
            running_count[i] += share_amt

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
        running_count = [0,0,0,0,0] 

        num[0] = n
        if testnum(num, running_count):
            print ("The Number Was %d" % n)
            print (running_count)

            total = sum(running_count)

            print ("Total %d, plus 5 for the monkey!"
                   " Original starting count %d" % (total, n))
            return

    print ("Not found in %d tries." % TESTQUANTITY)


if __name__=="__main__":
    main()
