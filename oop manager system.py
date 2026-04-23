# Name: Kaydan Venter
# Assignment: Manager and DepartmentManager Classes
# File Name: K_Venter_Program5.py
# Description: This program creates a Manager class and a subclass DepartmentManager.
# It allows the user to input manager and department details, then displays the data.

# Parent Class
class Manager:
    def __init__(self, name="", manager_id=""):
        self.__name = name
        self.__manager_id = manager_id

    # Mutators (Set methods)
    def set_name(self, name):
        self.__name = name

    def set_manager_id(self, manager_id):
        self.__manager_id = manager_id

    # Accessors (Get methods)
    def get_name(self):
        return self.__name

    def get_manager_id(self):
        return self.__manager_id


# Subclass
class DepartmentManager(Manager):
    def __init__(self, name="", manager_id="", dept_name="", num_employees=0):
        super().__init__(name, manager_id)
        self.__dept_name = dept_name
        self.__num_employees = num_employees

    # Mutators
    def set_dept_name(self, dept_name):
        self.__dept_name = dept_name

    def set_num_employees(self, num_employees):
        self.__num_employees = num_employees

    # Accessors
    def get_dept_name(self):
        return self.__dept_name

    def get_num_employees(self):
        return self.__num_employees


# Main Program
def main():
    # Create object
    manager = DepartmentManager()

    # User input
    name = input("Enter manager name: ")
    manager_id = input("Enter manager ID: ")
    dept_name = input("Enter department name: ")
    num_employees = int(input("Enter number of employees: "))

    # Store data using mutators
    manager.set_name(name)
    manager.set_manager_id(manager_id)
    manager.set_dept_name(dept_name)
    manager.set_num_employees(num_employees)

    # Display data using accessors
    print("\n--- Manager Information ---")
    print("Name:", manager.get_name())
    print("Manager ID:", manager.get_manager_id())
    print("Department:", manager.get_dept_name())
    print("Number of Employees:", manager.get_num_employees())


# Run program
main()
