d = {}
class Employee:
    def salary_slip(self,name,address,pan,basic,tds,deduct):
        self.name=name
        self.address=address
        self.pan=pan
        self.basic=basic
        self.tds=tds
        self.deduct=deduct
        self.hra=1.578*basic
        self.da=0.25*basic

        netsal=self.basic+self.hra+self.da-(self.deduct+self.tds)
        return netsal

    def accept(self):
        name=input("enter the name: ")
        address=input("enter the address: ")
        pan=input("enter the pan no.: ")
        basic=int(input("enter the basic: "))
        tds=int(input("enter the tds: "))
        deduct=int(input("enter the deduct: "))
        self.netsal=self.salary_slip(name,address,pan,basic,tds,deduct)

    def display(self):
        print("Name: ",self.name)
        print("Address: ",self.address)
        print("Pan:",self.pan)
        print("Basic: ",self.basic)
        print("tds: ",self.tds)
        print("Deduct: ",self.deduct)
        print("hra: ",self.hra)
        print("da: ",self.da)

    def search(self,name):
        for k,v in d.items():
            print(k,v)
            if k == name:
                v.display()

while True:
        print("1 => Accept the data")
        print("2 => Display the data")
        print("3 => Update dictionary")
        print("4 => Search in dictionary")
        print("5 => Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            print("Enter details: ")
            e1 =Employee()
            e1.accept()
        elif ch == 2:
            e1.display()
        elif ch == 3:
            d.update({e1.name:e1})
            print(d)
        elif ch == 4:
            name = input("Enter name for search: ")
            e1.search(name)
        elif ch == 5:
            break
        else:
            print("!!Invalid input")


