class Employee:
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname
    
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    @property
    def email(self):
        if(self.fname == None or self.lname == None):
            return "Email is not set"
        return f"{self.fname}.{self.lname}@gmail.com"
    
    @email.setter
    def email(self,email):
        name = email.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter
    def email(self):
        print("Email is deleting.....")
        self.fname = None
        self.lname = None
    


    

e1 = Employee("Rohit", "Udaiwal")
print(e1.explain())
e1.email = "vishnu.pillai@gmail.com"
print(e1.email)
print(e1.explain())
del e1.email
print(e1.email)

e1.email = "Ravleen.kaur@gmaill.com"
print(e1.email)