for x in range(1,10):
    for y in range(1,10):
        for z in range(1,10):
            for t in range(1,10):
                if 2005-(1000*x+100*y+10*z+t) == (x+y+z+t):
                    print (1000*x+100*y+10*z+t)