import pymongo

class Students:
    def __init__(self, name, age, pn, email, fathers_name, amka):
        self.connect_to_database = pymongo.MongoClient('mongodb://localhost:27017/')
        self.name = name
        self.age = age
        
        self.pn = pn
        self.email = email
        self.fathers_name = fathers_name
        self.amka = amka

    def create_student(self):
        global db
        global data
        db = self.connect_to_database['school']
       
        data = db['students']

        student_data = {
            'Students Name': self.name,
            'Students Age': self.age,
            'Students Phone Number': self.pn,
            'Students E-mail': self.email,
            'Students Fathers Name': self.fathers_name,
            'Students AMKA': self.amka

        }

        save_to_database = data.insert_one(student_data)

class Create_Student(Students):
    def __init__(self):
        super()

    def input_students(self):

        name = input('Add students name: ')
        age = int(input('Add students age: '))
        pn = int(input('Add students phone number: '))
        e_mail = input('Add students e-mail: ')
        fa_n = input('Add students e-mail: ')
        amka = int(input('Add students amka: '))