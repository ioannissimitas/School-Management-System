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
            'Students Email': self.email,
            'Students Fathers Name': self.fathers_name,
            'Students AMKA': self.amka

        }


        save_to_database = data.insert_one(student_data)

    def read_student_data(self):
        db.students.find()