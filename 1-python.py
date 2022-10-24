text = "this is not a reversed text"
def reverse(x):
    temp=''
    l=len(x)
    for i in range(l):
        temp+=x[l-i-1]
    return temp
    print("the reversed text is: "+reverse(text))
