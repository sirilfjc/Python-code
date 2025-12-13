# Parent class
class Employee:

    # Constructor: automatically called when object is created
    def __init__(self, name, emp_id, salary):
        self.name = name          # Public variable → accessible anywhere
        self._emp_id = emp_id     # Protected variable → accessible in class & child class
        self.__salary = salary   # Private variable → accessible only inside this class

    # Public method to display employee name
    def displayName(self):
        print("Name:", self.name)

    # Protected method to display employee ID
    # Can be accessed inside this class and its child class
    def _displayID(self):
        print("Employee ID:", self._emp_id)

    # Private method to display salary
    # Cannot be accessed directly outside this class
    def __displaySalary(self):
        print("Salary:", self.__salary)

    # Public method to access private method (Encapsulation)
    def accessSalary(self):
        self.__displaySalary()


# Child class inheriting from Employee
class Manager(Employee):

    # Constructor of child class
    def __init__(self, name, emp_id, salary, department):
        # Calling parent class constructor using super()
        super().__init__(name, emp_id, salary)
        self.department = department   # Public variable

    # Public method to display department
    def displayDepartment(self):
        print("Department:", self.department)

    # Public method to access protected method of parent class
    def accessID(self):
        self._displayID()


# Creating object of Manager class
m = Manager("Ananya", 101, 50000, "HR")

# Calling public method to display name
m.displayName()

# Calling method that accesses protected member
m.accessID()

# Calling method that accesses private member through encapsulation
m.accessSalary()

# Calling method to display department
m.displayDepartment()
