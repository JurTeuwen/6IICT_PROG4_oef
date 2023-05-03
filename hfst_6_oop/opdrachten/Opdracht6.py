import random

class Student:
    def __init__(self, naam):
        self.naam = naam
        getal = random.randint(1,10000)
        self.studentennummer = f"S{getal}"
        self.ingeschreven_cursussen = []

    def info(self):
        print(f"{self.naam} : {self.studentennummer}")

class Cursus:
    def __init__(self, naam):
        self.naam = naam
        getal = random.randint(1,10000)
        self.cursusnummer = f"C{getal}"

    def info(self):
        print(f"{self.naam} : {self.cursusnummer}")

student_namen = ["Jan", "Piet", "Joris", "Korneel"]
cursus_namen = ["Wisk", "Prog", "Netw", "Frans"]


student1 = Student("Jan")