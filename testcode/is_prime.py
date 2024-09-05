def is_prime(n):
    """Let k begin with 2 and let k goes through 
    all number below n. If n can be divided by k ,
    it is not prime"""


    k=2
    while k<n:
        if n%k==0:
           print('False')
           return None
        k+=1
    if k>=n:
        print('Ture')