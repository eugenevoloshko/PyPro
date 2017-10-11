f = open('List.txt')

a = f.readlines()

endi = len(a)

print(endi)

print(a[2])

endi = endi + 1

print(endi)

ii = 0
for i in a:
    s = a[ii]
    n = s.find('M')
    if n != -1:
        print(s)
    ii = ii + 1
