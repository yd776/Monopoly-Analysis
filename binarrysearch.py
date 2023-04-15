def binary_search(v, a):
    if not a:
        return False

    m = len(a) // 2

    if v == a[m]:
        return True
    elif v < a[m]:
        return binary_search(v, a[:m])
    else:
        return binary_search(v, a[m+1:])
a=[1,2,3,4]
print(binary_search(4,a))