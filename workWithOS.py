import os
os.system("ping 8.8.8.8 > test.txt")

print("test message")

f = open("test.txt")

a = f.readlines()

print(a[3])

os.system(r'C:\Windows\notepad.exe')
