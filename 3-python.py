no_list = [1,2,3,4]
def maximum(x):
    mx=0
    for a in x:
        if mx<a:
            mx=a
    return a
print(maximum(no_list))
