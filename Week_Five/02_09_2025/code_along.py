#  Creating __init__.py
class Student:
    def __init__(self, name, course, level):  # This runs automatically
        print("Creating a new student...")
        self.name = name
        self.course = course
        self.level = level
        print(f"Student {name} has been created!")
        
student1 = Student("Abdullateef Olajide", "CSC", "Graduate")
print(student1.name)
print(student1.course)



# How init and self work together
class NigerianStudent:
    def __init__(self, name, state, course):
        print(f"Step 1: Creating student objects...")
        self.name = name
        self.state_of_origin = state
        self.course = course
        self.student_id = self.generate_id()
        print(f"step 6: {self.name} from {self.state_of_origin} is ready!")


    def generate_id(self):
        import random
        return f"NCC/0000/{random.randint(1000, 9999)}"
    

student2 = NigerianStudent("Abioye Olajide", "Oyo", "Programming")
print(student2.name)
print(student2.student_id)


#  More Example
class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")
    

    def buy_airtime(self, amount):
        self.airtime += amount  # self ensures it goes to the RIGHT person
        return f"{self.name} now has ₦{self.airtime} airtime"
    

#  Creating multiple users
user1 = PhoneUser("Abioye Olajide", "MTN")
user2 = PhoneUser("Fope Eriife", "Airtel")


# Each person's actions affect their own account
print(user1.buy_airtime(500))
print(user2.buy_airtime(1000))
print(user1.airtime)
print(user2.airtime)


# Defining Attributes of a student
class Student:
    def __init__(self, name, course, level, state_of_origin, cgpa= 0.0):
        self.name = name                   
        self.course = course              
        self.level = level                
        self.state_of_origin = state_of_origin  
        self.cgpa = cgpa 

#  Creating a student object
Olajide = Student("Olajide Abioye", "Computer Science", "Graduate", "Oyo State", 4.50)

print(Olajide.name)
print(Olajide.level)
print(Olajide.cgpa)


# Types of Attributes
# 1. Instance Attributes - Unique to each object
student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos" )

print(student1.name)  
print(student2.name) 

# 2. class attributes - Shared by all objects of the class
# class Student:
#     university = "Federal University of agriculture, Abeokuta."  
    
    def __init__(self, name, course):
        self.name = name         
        self.course = course

student1 = Student("Anthony Johnson", "Engineering")
student2 = Student("Fadilat Hassan", "Medicine")
print(Student.university)     
print(student1.university)   
print(student2.university)

#  Methods: The Actions (What Objcts CAN DO)
class Student:
    def __init__(self, name, course, level):
        # Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False
    

#      # Method: action the student can do
    def pay_school_fees(self):                   
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
    
    # Method: another action
    def register_courses(self):                   
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course}"
        else:
            return f"{self.name} must pay school fees first!"
    
      # Method: calculates CGPA
    def calculate_cgpa(self, grades):           
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        return "No grades provided"
    
Abiodun = Student("Abiodun Akinola", "Gistology", 600)
print(Abiodun.pay_school_fees())        
print(Abiodun.register_courses())       
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5])) 

#  Types of Methods
# 1. Instance Methods - Work with specific object data
def pay_school_fees(self):
    return f"{self.name} has paid school fees now"

Abiodun = Student("Abiodun Akinola", "Gistology", 600)
print(pay_school_fees(Abiodun)) 

# 2. Class Methods - Work with class-level data
@classmethod
def get_university(cls):
    return cls.university

# 3. Static Methods - Don't need object or class data
@staticmethod
def academic_calendar():
    return "Academic session runs from September to July"


#  How Attributes and Methods work  together
class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        # ATTRIBUTES - What the account HAS
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()
    
    # METHODS - What the account can DO
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount  # Method changes attribute
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # Method changes attribute
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
        return "Insufficient funds or invalid amount"
    
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    
    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"
    
    # Creating and using the account
adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)
olajide_account = BankAccount("Abdullateef Abioye", "ALT Bank", 70000)

# Attributes (characteristics)
print(f"Owner: {adunni_account.owner}")
print(f"Bank: {adunni_account.bank_name}")
print(f"Account Number: {adunni_account.account_number}")

print(f"Owner: {olajide_account.owner}")
print(f"Bank: {olajide_account.bank_name}")
print(f"Account Number: {olajide_account.account_number}")

# Methods (actions)
print(adunni_account.deposit(25000))    
print(adunni_account.withdraw(10000))  
print(adunni_account.transfer(15000, "Sunday James"))  
print(adunni_account.check_balance())   

# Practice Exercise 1
class NaijaPhone:
    def __init__(self, brand, model, network_provider):
        self.brand = brand
        self.model = model
        self.network_provider = network_provider
        self.airtime_balance = 0
        self.data_balance = 0
        self.is_on = False
    
    def power_on(self):
        self.is_on = True
        return f"{self.brand} phone is now on. Network: {self.network_provider}"
    
    def buy_airtime(self, amount):
        self.airtime_balance += amount
        return f"₦{amount} airtime purchased. Balance: ₦{self.airtime_balance}"
    
    def make_call(self, number):
        if self.is_on and self.airtime_balance > 0:
            self.airtime_balance -= 10
            return f"Calling {number}... Remaining airtime: ₦{self.airtime_balance}"
        return "Cannot make call. Check phone power and airtime balance"
    
    def send_sms(self, message, number):
        if self.airtime_balance >= 4:
            self.airtime_balance -= 4
            return f"SMS sent to {number}: '{message}'. Remaining airtime: ₦{self.airtime_balance}"
        return "Insufficient airtime to send SMS"
    
ola_user = NaijaPhone("Redmi", "14C", "MTN")
print(ola_user.power_on())
print(ola_user.buy_airtime(200))
print(ola_user.make_call(8143055319))
print(ola_user.send_sms("I love you, mum", 8127309014))