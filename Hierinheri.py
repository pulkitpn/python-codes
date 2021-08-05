class Student:
    def __init__(self,usn=None,name=None,age=None,sem=None,fees=None,stipend=None):
        self.usn=usn
        self.name=name
        self.age=age
        self.sem=sem
        self.fees=fees
        self.stipend=stipend
class Ugstudent(Student):
    def getdata(self):
        self.usn=input("Enter the USN: ")
        self.name=input("Enter the Name: ")
        self.age=input("Enter the Age: ")
        self.sem=input("Enter the Sem: ")
        self.fees=input("Enter the Fees: ")
        self.stipend=input("Enter the Stipend: ")
    def display(self):
        print(self.usn)
        print(self.name)
        print(self.age)
        print(self.sem)
        print(self.fees)
        print(self.stipend)
class Pgstudent(Student):
    def getdata(self):
        self.usn=input("Enter the USN: ")
        self.name=input("Enter the Name: ")
        self.age=input("Enter the Age: ")
        self.sem=input("Enter the Sem: ")
        self.fees=input("Enter the Fees: ")
        self.stipend=input("Enter the Stipend: ")
    def display(self):
        print("-"*60)
        print("USN: ",self.usn)
        print("NAME: ",self.name)
        print("AGE: ",self.age)
        print("SEM: ",self.sem)
        print("FEES: ",self.fees)
        print("STIPEND: ",self.stipend)
        print("-"*60)
ug=Ugstudent()
pg=Pgstudent()
while True:
    print("1=>input ug")
    print("2=>input pg")
    print("3=>display ug")
    print("4=>display pg")
    print("0=>exit")
    ch=int(input("enter choice: "))
    if ch==1:
        ug.getdata()
    elif ch==2:
        pg.getdata()
    elif ch==3:
        ug.display()
    elif ch==4:
        pg.display()
    elif ch==0:
        exit()
    
        
        
