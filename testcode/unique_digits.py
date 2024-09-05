def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    k=0
    count=0
    while k<=9:
        if has_digits(n,k):
            count+=1
        k+=1
    print(count)

def has_digits(n,k):
    while n>0:
        if n%10==k:
            return True
        n=n//10
    return False
    
