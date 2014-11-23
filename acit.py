from itertools import combinations

def foo(x,y):
    if (x<1 or y<1):
        return 1
    else:
        t=foo(x-1,y)
        c=t+foo(x,y-1)

        return c

    
def foo1(x,y):
    l=len([x for x in combinations(xrange(x+y),y)])
    return l

def test(x,y):
    print foo(x,y),foo1(x,y)


    
