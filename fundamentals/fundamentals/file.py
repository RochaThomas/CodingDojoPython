num1 = 42 #variable declaration, primative data type number
num2 = 2.3 #variable declaration, primative data type number
boolean = True #variable declaration, primative data type boolean
string = 'Hello World' #variable declaration, primative data type string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, composite data type list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, composite data type dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, composite data type tuple
print(type(fruit)) #type check
print(pizza_toppings[1]) #access value of list
pizza_toppings.append('Mushrooms') #add value to list
print(person['name']) #access value of dictionary
person['name'] = 'George' #change value of dictionary
person['eye_color'] = 'blue' #add value to dictionary
print(fruit[2]) #access value of tuple

if num1 > 45: #conditional if
    print("It's greater")
else: # conditional else
    print("It's lower")

if len(string) < 5: #length check conditional if
    print("It's a short word!")
elif len(string) > 15: #length check conditional else if
    print("It's a long word!")
else: #length check conditional else
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5): #for loop, start 2, end 5
    print(x)
for x in range(2,10,3): #for loop, start 2, end 10, increment 3
    print(x)
x = 0 #while loop
while(x < 5): #while loop end 5
    print(x)
    x += 1 #while loop increment

pizza_toppings.pop() #delete value at the end of list
pizza_toppings.pop(1) #delete value of list at specified index

print(person) 
person.pop('eye_color') #delete value of dictionary
print(person)

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional if
        continue #for loop continue
    print('After 1st if statement')
    if topping == 'Olives': #conditional if
        break #for loop break

def print_hello_ten_times(): #function
    for num in range(10): #for loop
        print('Hello')

print_hello_ten_times() #function call

def print_hello_x_times(x): #function with parameter x
    for num in range(x): #for loop
        print('Hello')

print_hello_x_times(4) #function call with argument 4

def print_hello_x_or_ten_times(x = 10): #function with parameter x that defaults to ten when no argument is passed
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) #function call with argument 4

#multiline comment
"""
Bonus section 
"""
#single line comments
# print(num3) name error
# num3 = 72 variable declaration number
# fruit[0] = 'cranberry' TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) KeyError: 'favorite_team'
# print(pizza_toppings[7]) IndexError: list index out of range
#   print(boolean) IndentationError: unexpected indent
# fruit.append('raspberry') AttributeError: 'tuple' has no attribute 'append'
# fruit.pop(1) AttributeError: 'tuple' has no attribute 'pop'