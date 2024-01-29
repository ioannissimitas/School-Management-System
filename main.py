from student import Students
import pymongo

def main():
    print('Welcome to the School Adminstration System')
    
    choices = input('1) Students Menu\nChoose one of the available options: ')

    if choices == '1':
        studentsMenu = input('1) Create Student\n2) Read Student Data\n3) Update Student\n4) Delete Student\nChoose one of the available options: ')
        
        global Student

        if studentsMenu == '1':
            name = input('Add Student Name: ')
            age = int(input('Add Students Age: '))
            phoneNumber = int(input('Add Students Phone Number: '))

            email = input('Add Students E-mail: ')
            fathersName = input('Add Students Father Name: ')
            amka = int(input('Add Students amka: '))

            Student = Students(name, age, phoneNumber, email, fathersName, amka)
            Student.create_student()
        elif studentsMenu == '2':
            Student.





main()