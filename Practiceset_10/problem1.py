# Create a class “Programmer” for storing information of few programmers working at Microsoft
class Programmer:
    company = "Microsoft"
    def __init__(self,name,lang,salary):
        
        self.name = name
        self.lang = lang
        self.salary = salary

p = Programmer("Shruti","Python",3500000)
print(p.name,p.lang,p.salary,p.company)
h = Programmer("Himani","Javascript",3500000)
print(h.name,h.lang,h.salary,p.company)