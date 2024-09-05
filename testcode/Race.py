def race(x):
    y=1
    while not ( y>x and (y<2*x or y==2*x)):
        y+=1
        if y>2*x:
            return None
    return y

def race_2(count):
    k=0
    x=1
    while k<count:
        y=1
        while not ( y>x and (y<2*x or y==2*x)):
            y+=1
            if y>2*x:
                x+=1
        k+=1
        print(x , y  , k)
        x+=1

race_2(20)
        