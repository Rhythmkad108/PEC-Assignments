#Question 1
print('<<<<<<<Question 1>>>>>>>>-----')
given_string="Python is a case sensitive language"
#1(a)
leng_th=len(given_string)
print('(a)Length of given input string is ',leng_th)
#1(b)
print('(b)Reverse of the given input string is ',given_string[ : :-1])
#1(c)
new_string1=given_string[10:26]
print('(c)New stored string is- ',new_string1)
#1(d)
print('(d)Replaced string is- ',given_string.replace('a case sensitive','object oriented'))
#1(e)
print('(e)Index of substring "a" is ',given_string.find('a'))
#1(f)
print('(f)White spaces removed string is ',given_string.replace(' ',''))

#Question 2
print('<<<<<<<Question 2>>>>>>>>-----')
name='Rhythm Kad'
sid=21103113
department_name='Computer Science and Enginnering'
cgpa=9.9
print('Hey,%s'%name,'Here!')
print('My SID is %d'%sid)
print('I am from %s'%department_name,'department and my CGPA is %0.1f'%cgpa)

#Question 3
print('<<<<<<<Question 3>>>>>>>>-----')
a=56
b=10
#3(a)
print('(a) a&b= ',a&b)
#3(b)
print('(b) a|b= ',a|b)
#3(c)
print('(c) a^b= ',a^b)
#3(d)
print('(d) a<<2= ',a<<2)
print('    b<<2= ',b<<2)
#3(e)
print('(e) a>>2= ',a>>2)
print('    b>>4= ',b>>4)

#Question 4
print('<<<<<<<Question 4>>>>>>>>-----')
num1=int(input('Enter first number '))
num2=int(input('Enter second number '))
num3=int(input('Enter third number '))
list=[num1,num2,num3]
print('Greatest number is ',max(list))

#Question 5
print('<<<<<<<Question 5>>>>>>>>-----')
input_string=input('Enter your string. ')
if('name' in input_string):
    print('Yes')
else:
    print('No')

#Question 6
print('<<<<<<<Question 6>>>>>>>>-----')
len_gth1=float(input('Enter length of first side. '))
len_gth2=float(input('Enter length of second side. '))
len_gth3=float(input('Enter length of third side. '))
if(len_gth1+len_gth2<=len_gth3):
    print('Triangle with these side lengths is not possible.')
elif(len_gth1+len_gth3<=len_gth2):
    print('Triangle with these side lengths is not possible.')    
elif(len_gth3+len_gth2<=len_gth1):
    print('Triangle with these side lengths is not possible.')             
else:
    print('Triangle with side lengths %0.2f,'%len_gth1,'%.2f,'%len_gth2,'%.2f units is possible.'%len_gth3)

    
    
