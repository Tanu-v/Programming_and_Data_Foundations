# Polymorphism in Python OOP


# Created a base class named Women
class Women:
    def __init__(self, role, task):
        self.role = role
        self.task = task

    def move(self):
        print("Fulfilling daily responsibilities.\n")


class Daughter(Women):
    pass


class Student(Women):
    def move(self):
        print("Attending classes and studying for exams.\n")


class Mother(Women):
    def move(self):
        print("Nurturing and guiding children.\n")


class Doctor(Women):
    pass


class Writer(Women):
    def move(self):
        print("Drafting and publishing creative stories.\n")


class ContentCreator(Women):
    pass


# Created different objects
daughter1 = Daughter("ROLE OF A DAUGHTER: LISTEN TO PARENTS", "TASK: CARE FOR PARENTS.")
student1 = Student("ROLE OF A STUDENT: DO STUDIES", "TASK: PASS THE EXAMS.")
mother1 = Mother("ROLE OF A MOTHER: LOOK AFTER CHILDREN", "TASK: PROVIDE THEM GOOD MANNERS.")
doctor1 = Doctor("ROLE OF A DOCTOR: TREAT PATIENTS", "TASK: PROVIDE GOOD TREATMENT.")
writer1 = Writer("ROLE OF A WRITER: WRITE INTERESTING STORIES", "TASK: PROVIDE READERS SOMETHING INTERESTING TO READ.")
content_creator1 = ContentCreator("ROLE OF A CONTENT CREATOR: CREATE CONTENT", "TASK: PROVIDE USEFUL AND INTERESTING CONTENT.")

# Polymorphic loop calling the same method across different classes
for person in (daughter1, student1, mother1, doctor1, writer1, content_creator1):
    print(person.role)
    print(person.task)
    person.move()
