#function to handle number classification (even/odd).
def numberClassifier(num):
    if num % 2 == 0:
        print("The number is even")
    
    else:
        print("The number is odd") 
        
        
#Ask the user for an integer input and check if the number is even or odd.
thenumber = int(input("Enter a number:"))
result = numberClassifier(thenumber) 
print(result)

#for loop to generate a list of even numbers from 1 to 50 and prints the list
even_numbers = [num for num in range(1, 50) if num % 2 == 0]
print(even_numbers)

 
       
# while loop to print numbers from 10 down to 1 in reverse order.
j = 10
while j >= 1:
    print(j)
    j -= 1
   


    