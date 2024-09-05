def fizzbuzz(n):
    k=1
    while k<=n:
        if k%3==0 and k%5==0:
            print(k,'Fizzbuzz')
        elif k%3==0:
            print(k,'Fizz')
        elif k%5==0:
            print(k,'buzz')
        else:
            print(k,'i')
        k+=1

fizzbuzz(20)