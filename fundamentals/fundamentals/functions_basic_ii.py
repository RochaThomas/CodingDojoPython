
def countdown(n):
    result = []
    for i in range(n, -1, -1):
        result.append(i)
    return result

countdownList = countdown(10)
print(countdownList)

def two_num_list(l):
    print(l[0])
    return l[1]
x = two_num_list([2,7])
print(x)

def first_plus_length(l):
    return l[0] + len(l)
print(first_plus_length([1,0,0,0,0]))

def greater_than_second(l):
    result = []
    if len(l) < 2:
        return False
    else:
        for i in range(len(l)):
            if l[i] > l[1]:
                result.append(l[i])
    return result
greater_than_list = greater_than_second([3,2,4,1,6,1])
greater_than_list_false = greater_than_second([1])
print(greater_than_list)
print(greater_than_list_false)

def this_length_that_value(n, m):
    result = []
    for i in range(n):
        result.append(m)
    return result
myList = this_length_that_value(6,2)
print(myList)