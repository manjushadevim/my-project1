digit_count,num,l1 = int(input()),int(input()),[]
l = [1,2,3,4,5,6,7,8,9]

start,limit = l[:digit_count],l[len(l)-digit_count:]

def convert(list1):
    s = [str(i) for i in list1]
    res = int("".join(s))
    return res

def check(num):
    if len(set(list(num))) == len(num):
        return 1
    return 0

def previous(num,l1):
    if int(num) in l1:
        a = l1.index(int(num))
        return l1[a-1]
 
def next(num,l1):
    if num == l1[-1]:
        return l1[0]
    if int(num) in l1:
        a = l1.index(int(num))
        return l1[a+1]
    
for x in range(convert(start),convert(limit)+1):
    if list(str(x)) == sorted(str(x)) and x % 11 != 0 and check(str(x)):
        l1.append(x)
print()
print(previous(num,l1))
print(next(num,l1))


