# students = {
#     'name' : [],
#     'age' : [], 
# } 

# name = []
# age = []

# y=0

# while y < 4:
    

#     name1 = input('Enter Name ')
#     age1 = input('Enter age ')

#     name.append(name1)
#     age.append(age1)
#     y+=1
    
# students['name'] = [x for x in name]
# students['age'] = [i for i in age]

# print(students)

# import datetime


# dateTodayyear = datetime.date.today().year
# dateTodayDay = datetime.date.today().year
# dateTodayMonth = datetime.date.today().year


# studentDOBY = input('Enter the year you were born')
# studentDOBM = input('Enter the month you were born')
# studentDOBD = input('Enter the day you were born')

# def calAge():
#     # db = dateTodayDay - studentDOBD
#     # mb = dateTodayMonth - studentDOBM
#     yb = dateTodayyear - studentDOBY
    
#     print(yb)
    
# calAge

import datetime

def calAge():
    today = datetime.date.today()

    year = int(input('Enter the year you were born: '))
    month = int(input('Enter the month you were born: '))
    day = int(input('Enter the day you were born: '))

    dob = datetime.date(year, month, day)

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    print("Your age is:", age)

calAge()