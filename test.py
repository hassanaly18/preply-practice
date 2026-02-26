from colorama import Fore, Back, init, Style
init(autoreset=True)

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Classroom(Teacher):
    def __init__(self, name, subject):
        super().__init__(name, subject)
        self.students = []
    
    def add_student(self, name):
        self.students.append(name)
        print(Fore.CYAN + "Student", Fore.BLUE+ name ,Fore.CYAN + "added successfully")
    
    def show_details(self):
        print(Fore.GREEN+ Style.BRIGHT +"\n.....Classroom.....")
        print(Fore.YELLOW+"Teacher: "+ self.name)
        print("Students:")
        for student in self.students:
            print(Back.MAGENTA+"Student name:", Fore.RED + student)

c = Classroom("John", "Chemistry")

c.add_student("Mike")
c.add_student("Walter")
c.add_student("Doe")
c.add_student("Emma")

c.show_details()
