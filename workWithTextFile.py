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
        slotN = s[0:14]
        print(slotN)

        barCode = s[18:34]
        print(barCode)

        dateExp = s[36:56]
        print(dateExp)

        l = len(s)

        typeOfData = s[76:l]
        print(typeOfData)

        ltr = open('listToRemove.txt', 'a')

        ltr.write(slotN + '\n' + 'Barcode: ' + barCode + '\n' + 'Expire in: ' + dateExp + '\n' + 'Content: ' + typeOfData + '\n' + '\n')

    ii = ii + 1
