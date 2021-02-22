# Arrays - DS

# Complete the reverseArray function below.
def reverseArray(a):
    alen = len(a)
    newa = []
    while(alen):
        newa.append(a[alen - 1])
        alen -= 1
    return newa
