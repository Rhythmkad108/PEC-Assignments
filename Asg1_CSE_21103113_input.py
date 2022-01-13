#Question1
print('<<<<<[Question 1]>>>>>---------- ')
print('Enter three numbers.')
first_number=int(input('First number is '))
second_number=int(input('Second number is '))
third_number=int(input('Third number is '))
average=(first_number+second_number+third_number)/3
print('Average of the three numbers is:',average)

#Question 2
print('<<<<<[Question 2]>>>>>---------- ')
print('All money is in Dollars$')
gross_income=int(input('Gross income='))
tax_rate=20/100
standard_deduction=10000
deduction_per_dependent=3000
number_of_dependent=int(input('Number of Dependents='))
taxable_income=gross_income-standard_deduction-(deduction_per_dependent*number_of_dependent)
tax=taxable_income*tax_rate
print('Your Income Tax is:',tax)

#Question 3
print('<<<<<[Question 3]>>>>>---------- ')
print('Enter details. ')
Sid=input('Student iD:')
name=input('Name:')
gender=input('Gender(M for male,F for female,U for unknown):')
course_name=input('Course Name:')
cgpa=input('CGPA:')
print([Sid,name,gender,course_name,cgpa])
