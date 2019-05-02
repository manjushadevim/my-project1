p = 1
while(1):
    r = int(input())
    if r == 0:
        exit()
    else:
        c,l1 = int(input()),[]
        for i in range(r):
            l1.append(input())
    print('puzzle #',p)
    print('Across')
    for i in l1:
        i = i.split('*')
        while '' in i:
            i.remove('')
        for j in i:
            print(j)
    print('Down')
    for i in range(c):
        for j in range(r):
            if l1[j][i] == '*':
                print('')
            else:
                print(l1[j][i],end = '')
        print('')
    p += 1
