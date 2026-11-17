
#Taking user Input and Assigning Grade 

print("Please enter a four digit no. below:-")

avgmarks=int(input("Enter your marks here:"))

if  avgmarks >= 8200: 
    print("'O'('A+')")
if  avgmarks<8200 and avgmarks<=6279: 
    print("1st division('A')")  
if  avgmarks<6279 and avgmarks<=5259:
    print("2nd division('B')")  
if  avgmarks<5259 and avgmarks<=4249:
    print("3rd division('C')")
if  avgmarks<=239:
    print("Fail")