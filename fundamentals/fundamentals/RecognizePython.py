num1 = 42  # variable declaration Numbers
num2 = 2.3 # variable declaration Numbers
boolean = True # variable declaration Boolean
string = 'Hello World' # variable declaration Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #Tuples initialize
print(type(fruit)) # type check
print(pizza_toppings[1]) # List access value 
pizza_toppings.append('Mushrooms') #List add value
print(person['name']) # Dictionary access value
person['name'] = 'George' # Dictionary change value
person['eye_color'] = 'blue' # Dictionary add value
print(fruit[2]) # Tuples access value

if num1 > 45: # conditional if
    print("It's greater")
else: # conditional else
    print("It's lower")

if len(string) < 5: # conditional if
    print("It's a short word!")
elif len(string) > 15: # conditional else if
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # for loop start 0 stop 5 increment 1
    print(x)
for x in range(2,5): # for loop start 2 stop 5 increment 1
    print(x)
for x in range(2,10,3): # for loop start 2 stop 10 increment 3
    print(x)
x = 0 # while loop start 0 stop 5 increment 1
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() # List delete last value
pizza_toppings.pop(1) # List delete value at index 1

print(person) # print Dictionary
person.pop('eye_color') # Dictionary delete value eye_color
print(person) # print Dictionary

for topping in pizza_toppings: # for loop in List pizza_toppings
    if topping == 'Pepperoni': # conditional if topping equals Pepperoni continue
        continue 
    print('After 1st if statement') 
    if topping == 'Olives': # conditional if topping equals Olives break
        break

def print_hello_ten_times(): # function
    for num in range(10):
        print('Hello')

print_hello_ten_times() # function call

def print_hello_x_times(x): # function, parameter x
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # function call with parameter 4

def print_hello_x_or_ten_times(x = 10): # function with default parameter x with value 10
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # function call
print_hello_x_or_ten_times(4) # function call with parameter 4


# comment multiline
""" 
Bonus section 
"""

# print(num3) # NameError variable num3 is not defined
# num3 = 72
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # unexpected indent
# fruit.append('raspberry') # 'tuple' object has no attribute 'append'
# fruit.pop(1) # 'tuple' object has no attribute 'pop'