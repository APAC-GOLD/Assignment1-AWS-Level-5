# Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
# - Use 'assign_department' method to change the department of an employee.
# - Use 'print_employee_details' method to print the details of an employee.
# - Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked,
# which is the number of hours worked by the employee. If the number of hours worked is more than 50,
# the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
#
# ```
# overtime = hours_worked – 50
# overtime amount = (overtime * (salary / 50))
# ```
#
# ```
# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# "KING", "E5698", 20000, "RESEARCH"
# ```
class SalaryNotInRangeError(Exception):
    def __init__(self, message="Salary is not above minmun wage"):
        self.message = message
        super().__init__(self.message)
        # ========================================================================
class Employee:
    def __init__(self, name, emp_id, salary, department):
        # ========================================================================
        self.emp_id = emp_id
        self.emp_name = name
        self.emp_salary = salary
        self.emp_department = department
        # ========================================================================
        pass

    def calculate_salary(self, base_salary, hours_worked):
        # ========================================================================
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (base_salary / 50)
            final_salary = base_salary + overtime_amount
        else:
            final_salary = base_salary  
        # ========================================================================
    
        # Custom Exception in Python section 2.5
        if final_salary < 40000:
            raise SalaryNotInRangeError()
        return final_salary
    
        # ========================================================================

    def assign_department(self, emp_department):
        # ========================================================================
        self.emp_department = emp_department
        # ========================================================================
        pass

    def print_employee_details(self):
        # ========================================================================
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
        print("-----------------------")
        # ========================================================================
        pass


# Sample output
# ------------------------------------------------
# Original Employee Details:
#
# Name:  ADAMS
# ID:  E7876
# Salary:  50000
# Department:  ACCOUNTING
# ----------------------
#
# Name:  JONES
# ID:  E7499
# Salary:  45000
# Department:  RESEARCH
# ----------------------
#
# Name:  MARTIN
# ID:  E7900
# Salary:  50000
# Department:  SALES
# ----------------------
#
# Name:  SMITH
# ID:  E7698
# Salary:  55000
# Department:  OPERATIONS
# ------------------------------------------------
# Updated Employee Details:
#
# Name:  ADAMS
# ID:  E7876
# Salary:  50000
# Department:  OPERATIONS
# ----------------------
#
# Name:  JONES
# ID:  E7499
# Salary:  46800.0
# Department:  RESEARCH
# ----------------------
#
# Name:  MARTIN
# ID:  E7900
# Salary:  50000
# Department:  SALES
# ----------------------
#
# Name:  SMITH
# ID:  E7698
# Salary:  66000.0
# Department:  SALES
# ------------------------------------------------
def main():
    employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
    employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
    employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
    employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

    print("Original Employee Details:")
    employee1.print_employee_details()
    employee2.print_employee_details()
    employee3.print_employee_details()
    employee4.print_employee_details()

    # Change the departments of employee1 and employee4
    # employee2.calculate_salary(45000, 52)
    # eemployee4.calculate_salary(45000, 60)
    employee1.assign_department("OPERATIONS")
    employee4.assign_department("SALES")
    # print changes
    employee1.print_employee_details()
    employee4.print_employee_details()

    # Now calculate the overtime of the employees who are eligible:
    print("Overtime + Salary $")
    # employee2.calculate_salary(45000, 52)
    # employee4.calculate_salary(45000, 60)
    print(employee2.calculate_salary(45000, 52))
    print(employee4.calculate_salary(45000, 60))

    print("Updated Employee Details:")
    employee1.print_employee_details()
    employee2.print_employee_details()
    employee3.print_employee_details()
    employee4.print_employee_details()

    employee5 = Employee("KING", "E5698", 20000, "RESEARCH")


if __name__ == "__main__":
    main()
