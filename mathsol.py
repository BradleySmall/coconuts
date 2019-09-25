"""
Mathamatical solution
"""


def func(num):
    """
    Function to do the splits
    """
    if num % 5 == 1:
        return (num - 1) / 5 * 4
    return 0


NUM = 6
while True:
    if func(func(func(func(func(NUM))))):
        break
    NUM += 5

print(NUM)
