#Using python OOPs , created many classes and made an invitation card


print("~~~~~~~~~~ \tWELCOME TO BARSI FUCTION\t ~~~~~~~~~~\n\n")

print("*********\tIn memory of belated 'Mr DHANUK LAL LODHI'\t********\n\n")

print("~~~~~ \tInformation about guests\t ~~~~~\n")


#Creating a python class named guests

class guests: 
  def __init__(self, name, title, inf):
    self.name = name
    self.title = title
    self.inf = inf
  def __str__(self):
    return f"{self.name}({self.title}) {self.inf}"    


#Adding guests and printing them one by one

p1 =guests("Mrs. Meena bai verma", "Big daughter", "and family")

print(p1)

p2 =guests("Mrs. Uma bai verma", "Second daughter" , "and Family")
print(p2)

p3 =guests("Mrs. Gayatri verma", "Third daughter" , "and family")
print(p3)

p4 =guests("Mrs. Yashoda Verma", "Fourth Daughter" , "and family ")
print(p4)

p5 =guests("Guests from belargondi","Dadi's maternal family ","with their family ")
print(p5)

p6 =guests("Mr Mahaveer verma ","First son ","and their family ")
print(p6)

p7 =guests("Mr Bhagwati janghel ", "second son ","and their family ")
print(p7)

p8 =guests("Mr. Shiv das ","Mom's father", "with family")#workoholic
print(p8)

p9 =guests("Guests from Bharda","Chachi's maternal family","with their family")
print(p9)

p10 =guests("Mr. Pankaj kumar sahu", " My brother","with family")#we will always be happy to receive you as our guest pankaj ,if you'll be coming with everyone it'll make us happiest!
print(p10)

print("\nMany other guests are coming and all of you all welcome here\n\n")
print("~~~~~~\tInformation about workers\t~~~~~\n")

#creating a worker class

class workers: 
  def __init__(other, name,workis , inf):
    other.name = name
    other.workis = workis
    other.inf = inf
  def __str__(other):
    return f"{other.name}({other.workis}) {other.inf}"  
  
  
#Adding workers one by one 
 
w3 =workers("Catering","all catering work","has many workers") 
print(w3)

w4 =workers("food ", "made by villagers ", "helps in food distribution also ")
print(w4)

w1 =workers("Mr. Rati Yadav","helper ","comes with his family ")
print(w1)

w2 =workers("Mr. Sudama Verma ", "helper","comes with his family")
print(w2)

print("\nAnd many works are done and handled by many people\n")

print("\n\n~~~~~~~~ \t OWNED BY \t ~~~~~~~\n\n")

#creating a owner class

class owner: 
  def __init__(self, name, title, ):
    self.name = name
    self.title = title
    
  def __str__(self):
    return f"{self.name}({self.title})"  
  
#Adding values and printting them
 
o1 =owner("Mrs Binda bai Lodhi", "Wife")
print(o1) 

o2 =owner("Mr. Heera Ram Verma and Mrs Kanti Verma","third son and wife")
print(o2)

o3 =owner("Mr. ShivRam Janghel and Mrs Pramila janghel","fourth son and wife")
print(o3)

print(" \n\nIn waiting you all to come and in making this ocasion joyful \n\n") 

print("\t\t'THANKYOU'")



    