from operator import mul

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    total=n
    if k==0:
        return 1
    elif k==1:
        return n
    else:
        while k>1:
            k -= 1
            total = total*(n-1)
            n -= 1
        return total
    
    


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    total=0
    while y // 10 != 0:
        total = total + y % 10
        y = y // 10
    return total+ y % 10



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    i=n%10
    n=n//10
    j=n%10

    while n>=0:
        if i==8 and j==8:
            return True
        elif n!=0:
            i=j
            n=n//10
            j=n%10
        else:
            return False
        