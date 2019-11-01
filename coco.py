#!/usr/bin/python3
"""Solve the 5 men and the coconuts problem."""


def split_them(quant, running_count):
    """Split quantity keeping the running count.

    Take a quantity and return False if it is not one more than
    equally divisible by 5.

    Subtract 1 and subtract 1/5 of the remaining

    When the split is done, update the running count for whichever
    first zero value
    """
    if quant[0] % 5 != 1:
        return False

    share_amt = (quant[0]-1)//5
    for k in range(5):
        if running_count[k] == 0:
            running_count[k] = share_amt
            break
    quant[0] -= (1 + share_amt)
    return True


def test_num(num, running_count):
    """Test a number for validity in this scenario.

    For a given number test to see if it will succeed using the
    logic for split defined in split_them 5 times.

    Then test to see that it is equally divisible by 5

    When successful the running_count will be updated
    one last time for the final split.
    """
    for _ in range(5):
        if not split_them(num, running_count):
            return False

    if num[0] % 5 == 0:
        share_amt = num[0]//5

        running_count = [count + share_amt for count in running_count]

        # for i in range(5):
        #    running_count[i] += share_amt

        return True
    return False


def main():
    """Solve with brute force.

    Choose a number and see if the result can be found and return
    or print an error
    """
    test_quantity = 1000000

    num = [0]
    for test_value in range(1, test_quantity):
        running_count = [0, 0, 0, 0, 0]

        num[0] = test_value
        if test_num(num, running_count):
            print("The Number Was %d" % test_value)
            print(running_count)

            total = sum(running_count)

            print("Total %d, plus 5 for the monkey!"
                  " Original starting count %d" % (total, test_value))
            return

    print("Not found in %d tries." % test_quantity)


if __name__ == "__main__":
    main()
