import sqlite3
import pandas
def table_creation(cursor):
    try:
        cursor.execute("create table Departments(Department_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Department_name varchar(40))")
        cursor.execute("create table Employee(Name varchar(30),ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,salary INTEGER,Department_id integer,FOREIGN KEY(Department_id) REFERENCES Departments(Department_id))")
        connection.commit()
    except:
        pass
def employee_values():
    Name=input("Enter the employee name : ")
    Salary=int(input("enter the salary : "))
    Department_id=int(input("enter the Department id : "))
    cursor.execute("insert into Employee(Name,Salary,Department_id)values(?,?,?)",(Name,Salary,Department_id))
    connection.commit()
    print("data enterd successfully. ")
def department_values(Department_name):
    cursor.execute("insert into Departments(Department_name)values(?)", (Department_name,))
    connection.commit()
    print("data enterd successfully. ")
def add_colm():
    try:
        cursor.execute("alter table Employee add City varchar(10)")
        connection.commit()
    except:
        pass
def name_employee():
    print("\nThe Employee details\n***********************************************")
    print(pandas.read_sql_query("select * FROM Employee where Name LIKE 'j%'", connection))
def name_update():
    id = input("\nEnter the Employee Id  :")
    name=input("enter the Name to edit : ")
    City=input("enter the City to edit : ")
    cursor.execute("UPDATE Employee SET Name='%s',City='%s' WHERE Id='%s'" %(name,City,id))
    connection.commit()
    print("The name was updated")
def employee_id():
    id = input("\nEnter the Employee Id  :")
    print("\nThe Employee details\n***********************************************")
    print(pandas.read_sql_query("select * from Employee where Id=%s" % (id), connection))

def department_employee():
    id=int(input(" \nEnter the department ID : "))
    print("\nThe Employee details\n***********************************************")
    print(pandas.read_sql_query("select * from Employee INNER JOIN Departments ON Employee.Department_Id=Departments.Department_Id WHERE  Employee.Department_Id=%s" %(id), connection))

if __name__ == "__main__":
    connection = sqlite3.connect("Company_db")
    cursor = connection.cursor()
    table_creation(cursor)
    request = input('\nDo you want to add new Department (y/n) ?')
    if request == 'y' or request == 'yes':
        Department_name = input("\nenter the department name : ")
        department_values(Department_name)
    else:
        pass
    while True:
        request = input('\nDo you want to add new employee (y/n) ?')
        if request == 'y' or request == 'yes':
            inputs = int(input("\nEnter the number of records to be inserted : "))
            for i in range(inputs):
                employee_values()
        break
    add_colm()
    print("\nThe Employee details\n***********************************************")
    print(pandas.read_sql_query("select Name,ID,Salary from Employee",connection))
    name_employee()
    employee_id()
    name_update()
    department_employee()