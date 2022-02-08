
for i in range(151):
    print(i)

for i in range(5,1001, 5):
    print(i)

for i in range(101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(1, 500000, 2):
    sum += i
print(sum)

for i in range(2018, 0, -4):
    print(i)

lowNum = 15
highNum = 100
mult = 7
for i in range(lowNum, highNum):
    if i % mult ==0:
        print(i)