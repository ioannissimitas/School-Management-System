from student import Students
import pymongo

def main():
    print('Welcome to the School Adminstration System')
    choices = input('1) Create Student\nChoose one of the available options: ')



    if choices == '1':
        name = input('Add students name: ')
        age = input('Add students age: ')
        phone = input('Add students phone number: ')
        email = input('Add students email: ')
        fathers_name = input('Add fathers name: ')
        amka = input('Add students amka: ')


        
        student = Students(name, age, phone, email, fathers_name, amka)
        student.create_student()

main()