class HR:
    def __init__(self, name, Id, salary, attendance, chutti, hours):
        self.name = name
        self.Id = Id
        self.salary = salary
        self.attendance = attendance
        self.chutti = chutti
        self.hours = hours

    def cmp_email(self):
        print(self.name, "@gamil.com")

    def yearSalary(self):
        print(self.name, "your yearly salary", self.salary * 12)

    def attendanceCalcu(self, Leaves):
        self.Leaves = Leaves
        print(self.name, "your total attendance=", self.attendance - self.Leaves)

    def taxcalcu(self, per):
        self.per = per
        tax = self.salary * (per / 100)
        print(self.name, "your monthly salary after applying tax=", self.salary - tax)

    def deductsalary(self, per):
        self.per = per
        tax = self.salary * (per / 100)
        if self.chutti > 3:
            self.chutti = self.chutti - 3
            print("Monthly salary after deduction of non paid leave=", (self.salary - tax) - (200 * self.chutti))

    def overtimesalary(self, per):
        self.per = per
        tax = self.salary * (per / 100)
        print("monthly salary after overtime=", (self.salary - tax)-(self.chutti*200) + (600 * self.hours))

name = input("enter your name=")
ID = int(input("enter your ID="))
salaary = int(input("Enter your Monthly salary="))
attend = int(input("No of days in this month="))
chutti = int(input("enter this month chutti="))
taax = int(input("enter tax ="))
hours = int(input("enter number of overtime hours="))

obj = HR(name, ID, salaary, attend, chutti, hours)
obj.cmp_email()
obj.yearSalary()
obj.attendanceCalcu(chutti)
obj.taxcalcu(taax)
obj.deductsalary(taax)
obj.overtimesalary(taax)