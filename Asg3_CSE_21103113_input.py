#Question 1
print('<<<<<<<<Question 1>>>>>>>>>')
inp_string=input('Enter string:')
inp_string=inp_string.lower()
list1=inp_string.split() #Create a list of the input string to check
                         #how many words there are in it.
if len(list1)==1:
    list11=list(inp_string)
    set11=set(list11)  #Create a set to print every item once.
    for letter in set11:
        print(letter,list11.count(letter))
    
else:
    set2=set(list1)   #Create a set to print every item once.
    for item in set2:
       print(item ,list1.count(item))


#Question 2        
print('<<<<<<<<Question 2>>>>>>>>>')
print('Message: Enter the Month in numerical form')
date=int(input('Enter Date:'))
month=int(input('Enter Month:'))
print('Message:The program works for all years>=1800 and years<=2025.') 
year=int(input('Enter Year:'))
if 1800<=year<=2025 :
    if 1<=month<=12:
        if 1<=date<=27:
            print('Next date is:',date+1,month,year)
        elif date==28:
            if month==1 or 3<=month<=12:
                print('Next date is:',date+1,month,year)
            else:
                if year%4==0:
                    print('Next date is:',29,2,year)
                else:
                     print('Next date is:',1,3,year)
        elif date==29:
            if month==1 or 3<=month<=12:
                print('Next date is:',30,month,year)
            else:
                if year%4==0:
                    print('Next date is:',1,3,year)
                else:
                    print('INVALID DATE ENTERED.')
        elif date==30:
            if month in [1,3,5,7,8,10,12]:
                print('Next date is:',31,month,year)
            elif month in [4,6,9,11]:
                print('Next date is:',1,month+1,year)
            else:
                print('INVALID DATE ENTERED.')
        elif date==31:
            if month in [1,3,5,7,8,10]:
                print('Next date is:',1,month+1,year)
            elif month==12:
                print('Next date is:',1,1,year+1)
            else:
                print('INVALID DATE ENTERED.')
        else:
            print('INVALID DATE ENTERED.')
    else:
        print('INVALID DATE ENTERED.')
else:
    print('RESTRICTED! Date entered is out of capacity of the program')


#Question 3
print('<<<<<<<<Question 3>>>>>>>>>')
inp_list=list()
out_list=list()
no_of_elements=int(input('Enter the number of numbers you want to add in the list. '))
i=0
while (i<no_of_elements):
    elements=inp_list.append(int(input('Enter number:')))
    i+=1
print('Your entered list:',inp_list)
j=0
while (j<no_of_elements):
    elements1=out_list.append((inp_list[j],inp_list[j]*inp_list[j]))
    j+=1
print('Final list is:',out_list)  
            

#Question 4
print('<<<<<<<<Question 4>>>>>>>>>')
dict1={10:'Outstanding',9:'Excellent',8:'Very Good',7:'Good',6:'Average',5:'Below Average',4:'Poor'}
dict2={10:'\'A+\'',9:'\'A\'',8:'\'B+\'',7:'\'B\'',6:'\'C+\'',5:'\'C\'',4:'\'D\''}
inp_grd_point=int(input('Enter your Grade Point: '))
print('Your Grade is %s'%dict2[inp_grd_point],'and %s'%dict1[inp_grd_point],'performance.') 


#Question 5
print('<<<<<<<<Question 5>>>>>>>>>')
string='ABCDEFGHIJK'
str2='          '
j=0  #i and j are defined to run loop
i=0  #and give location of strings. Thus these variables don't have literal meaning.
while (j<6):
    while (i<6):
        print(str2[ :i],string[ :11-2*j])
        i+=1
        j+=1


#Question 6
print('<<<<<<<<Question 6>>>>>>>>>')
directory=dict()
while(True):
    decision=input('Do you want to add information of students?\n(Y for Yes and N for No) ')
    if decision=='Y':
        key=int(input('Enter SID:'))
        print('Message:First letter of name should be capital')
        value=input('Enter Name:')
        directory[key]=value
    elif decision=='N':
        break
    else:
        print('Error')
#Question 6(a)
if len(directory)!=0:        
    print('(a)Student details:',directory)
else:
    print('(a)No information avaliable.')
help(sorted)#Explaining the sorted function
#Question 6(b)
print('(b)Ascending order:',dict(sorted(directory.items(),key=lambda x:x[1])))
print('   Descending order:',dict(sorted(directory.items(),key=lambda x:x[1],reverse=True)))
#Question 6(c)
print('(c)Ascending order:',dict(sorted(directory.items())))
print('   Descending order:',dict(sorted(directory.items(), reverse=True)))        
#Question 6(d)
key1=int(input('Enter Sid:'))
if key1 in list(directory):
    print('(d)',key1,directory[key1])
else:
    print('Invalid SID')



#Question 7
print('<<<<<<<<Question 7>>>>>>>>>')
print('The first and second term of Fibonacci Sequence is 1 and 1 respectively.')
print('Enter a number greater than or equal to 2')
no_of_terms=int(input('Enter the number of terms of Fibonacci sequence you want to print:'))
listof_FSeq=[1,1]  #defining the first 2 elements in the list of Fibonacci Sequence
r=2   #non literal variable defining index of list
while (2<=r<no_of_terms):
    listof_FSeq.insert(r,listof_FSeq[r-2]+listof_FSeq[r-1])
    r+=1
print(listof_FSeq)
print('Average of the series is:',sum(listof_FSeq)/len(listof_FSeq))


#Question 8
print('<<<<<<<<Question 8>>>>>>>>>')
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
#Question 8(a)
set_a=Set1^Set2
print('(a)Required set is:',set_a)
#Question 8(b)
set_b=Set1^Set2^Set3
print('(b)Required set is:',set_b)
#Question 8(c)
set_c=(Set1&Set2)|(Set2&Set3)|(Set1&Set3) #took common from each pair then union 
print('(c)Required set is:',set_c)
#Question 8(d)
extra_set={1,2,3,4,5,6,7,8,9,10}
set_d=extra_set-Set1   
print('(d)Required set is:',set_d)
#Question 8(e)
extra_set={1,2,3,4,5,6,7,8,9,10}
xtraset= Set1|Set2|Set3           
set_e=extra_set-xtraset
print('(e)Required set is:',set_e) 














             
