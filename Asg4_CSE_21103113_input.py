#Question 1
print('Question 1')
no_ofdisks=int(input('Enter the number of disks to be used:'))
def TowerOfHanoi(no_ofdisks,start_rod,end_rod,xtra_rod):
    if no_ofdisks==0:
        return
    TowerOfHanoi(no_ofdisks-1,start_rod,xtra_rod,end_rod)
    print(f'Move Disk {no_ofdisks} from rod {start_rod} to rod {end_rod}')
    TowerOfHanoi(no_ofdisks-1,xtra_rod,end_rod,start_rod)
TowerOfHanoi(no_ofdisks,'A','C','B')


#Question 2
print('Question 2')
from math import factorial
no_ofrows=int(input('Enter the number of rows of Pascal\'s Triangle you want to print:'))
print('Method 1: Using For Loop')
for i in range(no_ofrows):   
    for j in range(no_ofrows-i+1):
        print(end=" ")   # for left spacing
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")  # nCr = n!/((n-r)!*r!)
    print()  # for new line
print('Method 2:Using While Loop')
i=0
while(i<no_ofrows):
    z=no_ofrows-i+1
    while(z>0):
        print(end=" ")
        z-=1
    y=0
    while(y<i+1):
        print(factorial(i)//(factorial(y)*factorial(i-y)),end=" ")
        y+=1
    i+=1
    print()
print('Method 3:Using Recursion')
def PascalTriangle(no_ofrows,originalength=no_ofrows):
    if no_ofrows == 0:
        return
    PascalTriangle(no_ofrows-1,originalength)
    print('  '*(originalength-no_ofrows),end='')  #printing the spaces
    start = 1  #first number is always 1
    for i in range(1, no_ofrows+1):
        print(start, end ='   ')
        start = start*(no_ofrows-i)//i  #using Binomial Coefficient
    print()
PascalTriangle(no_ofrows)
  

#Question 3
print('Question 3')
int1, int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2
Remainder = int1 % int2

#Question 3(a)
print("(a)Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#Question 3(b)
if (Quotient == 0):
    print("(b) The quotient is zero")
if (Remainder == 0):
    print("(b)The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("(b) All the values are non zero")

#Question 3(c)
Clist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(Clist)):
    if Clist[i] > 4:
        result.append(Clist[i])
print(f"(c)Filtered out numbers that are greater than 4 are : {result}")

#Question 3(d)
setresult = set(result)
print("(d) Set:",setresult)

#Question 3(e)
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print("(e) Immutable set:",immutableSet)

#Question 3(f)
print("(f) Hash value of the max value from the above set:", hash(max(immutableSet)))


#Question 4
print('Question 4')
class Student:
    def __init__(self,name,rollno):
        self.name= name
        self.rollno= rollno
        print(f'The name of the student is {self.name} and his/her Roll number is {self.rollno}')
    def __del__(self):
       print('The Object has been deleted.')
std1=Student('Rhythm',21103113)
del std1


#Question 5
print('Question 5')
class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary= salary
    def printdetails(self):
        return f"The salary of {self.name} is INR {self.salary} monthly."

mehak=Employee('Mehak',40000)
ashok=Employee('Ashok',50000)
viren=Employee('Viren',60000)
print(mehak.printdetails())
print(ashok.printdetails())
print(viren.printdetails())


#Question 5(a)
mehak.salary=70000
print(f'(a)(UPDATED){mehak.printdetails()}')
#Question 5(b)
del viren
try:
    print(viren)
except:
    print('(b)(DELETED)The object viren was not found.')


#Question 6
print('Question 6')
def anagrams(word):
    if word=='':
        return [word]
    else:
        answer=[]
        for w in anagrams(word[1: ]):
            for u in range(len(word)+1):
                answer.append(w[ :u]+word[0]+w[u: ])
        return answer
print('Enter valid one word only!')
word=input('Enter the word by Player1 ')
response=input('Enter the word given by Player2:')
if response in anagrams(word):
    ques=input('Is the word entered a meaningful one?(Y for Yes /N for No)')
    if ques=='Y':
        print('The friendship is real!')
    else:
        print('The friendship is fake!')
else:
    print('Invalid Word Entered!')
    

