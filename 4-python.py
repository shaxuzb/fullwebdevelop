no_list = [22,22,2,1,11,11,2,2,3,3,3,4,5,5,5,55,55,66]
def unique_list(l):
    unil=[]
    for a in no_list:
        if a not in unil:
            unil.append(a)
    return unil
print(unique_list(no_list))
