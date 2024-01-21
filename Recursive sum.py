#calculate the sum of all values with recursive method
d = {'a':1, 'b':{'b1':1}, 'c':{'c1':1, 'c2':{'c21':1, 'c22':1}}}
def F(d):
    s = 0
    for e in d:
        if type(d[e]) == dict:
            s += F(d[e])
        else:
            s += d[e]
    return s
print(F(d))