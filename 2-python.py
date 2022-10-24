no_list = [22,68,90,78,90,88]
def average(x):
    av=0
    for a in x:
        av+=a
    av=av/len(x) 
    return av
print(average(no_list))
