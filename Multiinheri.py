class Student:
    def __init__(self,usn=None,name=None,age=None,math=None,lss=None,cn=None,oop=None,wap=None):
        self.usn=usn
        self.name=name
        self.age=age
        self.math=math
        self.lss=lss
        self.cn=cn
        self.oop=oop
        self.wap=wap
class Marks(Student):
    def __init__(self,total=None,percent=None):
        self.total=total
        self.percent=percent
    def getmarks(self):
        self.usn=input("Enter usn: ")
        self.name=input("Enter name: ")
        self.age=input("Enter age: ")
        self.math=int(input("Enter math mark: "))
        self.lss=int(input("Enter lss mark: "))
        self.cn=int(input("Enter cn mark: "))
        self.oop=int(input("Enter oop mark: "))
        self.wap=int(input("Enter wap mark: "))
        self.total=self.math+self.lss+self.cn+self.oop+self.wap
        self.percent=((self.math+self.lss+self.cn+self.oop+self.wap)/500)*100
class Showmark(Marks):
    def display(self):
        print("usn: ",self.usn)
        print("name: ",self.name)
        print("age: ",self.age)
        print("math: ",self.math)
        print("lss: ",self.lss)
        print("cn: ",self.cn)
        print("oop: ",self.oop)
        print("wap: ",self.wap)
        print("Total= ",self.total,"/500")
        print("Percentage= ",self.percent)
s1=Showmark()
while True:
    print("1=>input: ")
    print("2=>show: ")
    print("0=>exit")
    ch=int(input("enter choice: "))
    if ch==1:
        s1.getmarks()
    elif ch==2:
        s1.display()
    elif ch==0:
        exit()
