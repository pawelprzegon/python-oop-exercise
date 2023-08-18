# Write your code here!
class Member:
    def __init__(self, name):
        self.full_name = name

    def introduce(self):
        print(f'Hi, I\'m {self.full_name}!')


class Student(Member):
    def __init__(self, name, reason):
        super().__init__(name)
        self.reason = reason


payvand = Student('Payvand', 'Money')


class Instructor(Member):
    def __init__(self, name, bio, skillset):
        super().__init__(name)
        self.bio = bio
        self.skillset = skillset

    def add_skill(self, skill):
        self.skillset.append(skill)


brandon = Instructor('Brandon', 'I am a genius', ['React', 'Node', 'C'])


class Workshop():
    def __init__(self, date, subject, instructors, students):
        self.date = date
        self.subject = subject
        self.instructors = instructors
        self.students = students

    def add_participant(self, participant):
        if participant.__class__.__name__ == 'Instructor':
            self.instructors.append(participant)
        if participant.__class__.__name__ == 'Student':
            self.students.append(participant)

    def __workshop_details(self):
        print(f'Workshop - {self.date} - {self.subject}')

    def __students_details(self):
        print('\nStudents')
        for i, s in enumerate(self.students):
            print(f'{i + 1}. {s.full_name} - {s.reason}')

    def __instructors_details(self):
        print('\nInstructors')
        for i, inst in enumerate(self.instructors):
            print(f"{i + 1}. {inst.full_name} - {', '.join(list(inst.skillset))}")
            print(f'\t{inst.bio}')

    def get_details(self):
        self.__workshop_details()
        self.__students_details()
        self.__instructors_details()





# sei=Workshop('12/12/19', 'SEI', [], [])
# sei.add_participant(brandon)
# sei.add_participant(payvand)
# sei.print_details()

workshop = Workshop("12/03/2014", "Shutl", [], [])

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Ruby", "I want to help people learn coding.", [])
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love", [])
nicole.add_skill("Ruby")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.get_details()
