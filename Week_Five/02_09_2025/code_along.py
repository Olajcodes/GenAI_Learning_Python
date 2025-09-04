#  Creating __init__.py
# class Student:
#     def __init__(self, name, course, level):  # This runs automatically
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created!")
        
# student1 = Student("Abdullateef Olajide", "CSC", "Graduate")
# print(student1.name)
# print(student1.course)



# # How init and self work together
# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Creating student objects...")
#         self.name = name
#         self.state_of_origin = state
#         self.course = course
#         self.student_id = self.generate_id()
#         print(f"step 6: {self.name} from {self.state_of_origin} is ready!")


#     def generate_id(self):
#         import random
#         return f"NCC/0000/{random.randint(1000, 9999)}"
    

# student2 = NigerianStudent("Abioye Olajide", "Oyo", "Programming")
# print(student2.name)
# print(student2.student_id)


# #  More Example
# class PhoneUser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f"{self.name} joined {self.network} network")
    

#     def buy_airtime(self, amount):
#         self.airtime += amount  # self ensures it goes to the RIGHT person
#         return f"{self.name} now has ₦{self.airtime} airtime"
    

# #  Creating multiple users
# user1 = PhoneUser("Abioye Olajide", "MTN")
# user2 = PhoneUser("Fope Eriife", "Airtel")


# # Each person's actions affect their own account
# print(user1.buy_airtime(500))
# print(user2.buy_airtime(1000))
# print(user1.airtime)
# print(user2.airtime)


# Defining Attributes of a student
# class Student:
#     def __init__(self, name, course, level, state_of_origin, cgpa= 0.0):
#         self.name = name                   
#         self.course = course              
#         self.level = level                
#         self.state_of_origin = state_of_origin  
#         self.cgpa = cgpa 

# #  Creating a student object
# Olajide = Student("Olajide Abioye", "Computer Science", "Graduate", "Oyo State", 4.50)

# print(Olajide.name)
# print(Olajide.level)
# print(Olajide.cgpa)


# Types of Attributes
# 1. Instance Attributes - Unique to each object
# student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
# student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos" )

# print(student1.name)  
# print(student2.name) 

# 2. class attributes - Shared by all objects of the class
# class Student:
#     university = "Federal University of agriculture, Abeokuta."  
    
#     def __init__(self, name, course):
#         self.name = name         
#         self.course = course
# student1 = Student("Anthony Johnson", "Engineering")
# student2 = Student("Fadilat Hassan", "Medicine" )
# print(Student.university)     
# print(student1.university)   
# print(student2.university)

#  Methods: The Actions (What Objcts CAN DO)
class Student:
    def __init__(self, name, course, level):
        # Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False
    

     # Method: action the student can do
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
    
# Using methods
Abiodun = Student("Abiodun Akinola", "Gistology", 600)
print(Abiodun.pay_school_fees())        
print(Abiodun.register_courses())       
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5])) 

# Types of Methods
# 1. Instance Methods - Work with specific object data
# 'self' refers to the specific student
def pay_school_fees(self):  
    return f"{self.name} has paid school fees"

