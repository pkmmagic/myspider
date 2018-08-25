
def g():
    def fab(): 
        n = 0
        a = 1
        while n < 10: 
            yield a 
            a += n 
            n = n + 1
    t = fab()
    return t.__next__()
