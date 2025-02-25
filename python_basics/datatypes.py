#Creates at least one variable of each data type: int, float, complex, list, tuple, dict, set, and bool.

age = 15    #int 
price  = 150.50  #float
myNum = 2j   #complex
names = ["John", "Peter", "Mark", "Harry" ]  #list
fruits = ("apple", "banana", "orange" "mango")  #tuple
capitalCities = {      #dict
    "Kenya" : "Nairobi",
    "Uganda" : "Kampala",
    "Tanzania" : "Dodoma",
    "Sudan" : "Khartoum"
}

mySet = {2, 4, 6, 8}  #set
thisbool = True    #bool

 #print type of each variable
print(type(age))
print(type(price))
print(type(myNum))
print(type(names))
print(type(fruits))
print(type(capitalCities))
print(type(mySet))
print(type(thisbool))


x = float(age) #integer variable to float
y = int(price) #float variable to integer
z = complex(age) #integer variable to complex


#results
print(x)
print(y)
print(z)

