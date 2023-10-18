# Here x is a new reference to same list 1st
def myFun(x):
    x[0] = 20
    x = []

# Driver Code (Note that is 1st modified)
# After function call
list = list(range(10, 15))
myFun(list)
print(list)