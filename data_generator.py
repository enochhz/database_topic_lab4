from pg_manager import PostgreSQLManger
import datetime
import random

# Database Initialization
postgresSQLManager = PostgreSQLManger()

# Drop all tables_dic
employee_table = "Employee"
project_table = "Project"
assignment1_table = "Assignment1"
assignment2_table = "Assignment2"
projectlist1_table = "ProjectList1"
projectlist2_table = "ProjectList2"
employeelist1_table = "EmployeeList1"
employeelist2_table = "EmployeeList2"
empass1_table = "EmpAss1"
empass2_table = "EmpAss2"
projectass1_table = "ProjectAss1"
projectass2_table = "ProjectAss2"
tables = [employee_table, project_table, assignment1_table, assignment2_table, 
          projectlist1_table, projectlist2_table, employeelist1_table, employeelist2_table,
          empass1_table, empass2_table, projectass1_table, projectass2_table]
tables_dic = {}
for table in tables:
    tables_dic[table] = {"table": None, "data": []}

# for key in tables_dic.keys():
postgresSQLManager.drop_table(empass1_table)
postgresSQLManager.drop_table(empass2_table)
postgresSQLManager.drop_table(projectlist1_table)
postgresSQLManager.drop_table(projectlist2_table)
postgresSQLManager.drop_table(projectass1_table)
postgresSQLManager.drop_table(projectass2_table)
postgresSQLManager.drop_table(employeelist1_table)
postgresSQLManager.drop_table(employeelist2_table)
postgresSQLManager.drop_table(assignment1_table)
postgresSQLManager.drop_table(assignment2_table)
postgresSQLManager.drop_table(employee_table)
postgresSQLManager.drop_table(project_table)

# Tables Initialization
tables_dic[employee_table]["table"] = {
    "IDE": ["integer", 1],
    "Name": ["text", 0],
    "Address": ["text", 0],
    "Age": ["integer", 0],
    "Position": ["text", 0],
    "WagesPerHour": ["integer", 0],
}
tables_dic[project_table]["table"] = {
    "IDP": ["integer", 1],
    "Title": ["text", 0],
    "StartingDate": ["DATE", 0],
}
tables_dic[assignment1_table]["table"] = {
    "IDE": ["integer", 1, f"{employee_table}(IDE)"],
    "IDP": ["integer", 1, f"{project_table}(IDP)"],
    "NumberOfHours": ["integer", 0],
}
tables_dic[assignment2_table]["table"] = {
    "IDE": ["integer", 1, f"{employee_table}(IDE)"],
    "Name": ["text", 0],
    "WagesPerHour": ["integer", 0],
    "IDP": ["integer", 1, f"{project_table}(IDP)"],
    "Title": ["text", 0],
    "NumberOfHours": ["integer", 0],
}
tables_dic[projectlist1_table]["table"] = {
    "IDP": ["integer", 0, f"{project_table}(IDP)"],
    "NumberOfHours": ["integer", 0]
}
tables_dic[projectlist2_table]["table"] = {
    "IDP": ["integer", 0, f"{project_table}(IDP)"],
    "Title": ["text", 0],
    "NumberOfHours": ["integer", 0]
}
tables_dic[employeelist1_table]["table"] = {
    "IDE": ["integer", 1, f"{employee_table}(IDE)"],
    "NumberOfHours": ["integer", 0],
    "WagesPerHour": ["integer", 0]
}
tables_dic[employeelist2_table]["table"] = {
    "IDE": ["integer", 1, f"{employee_table}(IDE)"],
    "Name": ["text", 0],
    "NumberOfHours": ["integer", 0],
    "WagesPerHour": ["integer", 0]
}
tables_dic[empass1_table]["table"] = {
    "IDE": ["integer", 1, f"{employee_table}(IDE)"],
    "Address": ["text", 0],
    "Age": ["integer", 0],
    "Position": ["text", 0],
    "WagesPerHour": ["integer", 0],
    "AssignedProjects": [projectlist1_table + "[]", 0],
}
tables_dic[empass2_table]["table"] = {
    "IDE": ["integer", 1, f"{employee_table}(IDE)"],
    "Name": ["text", 0],
    "Address": ["text", 0],
    "Age": ["integer", 0],
    "Position": ["text", 0],
    "WagesPerHour": ["integer", 0],
    "AssignedProjects": [projectlist2_table + "[]", 0],
}
tables_dic[projectass1_table]["table"] = {
    "IDP": ["integer", 1, f"{project_table}(IDP)"],
    "StartingDate": ["DATE", 0],
    "Employees": [employeelist1_table + "[]", 0],
}
tables_dic[projectass2_table]["table"] = {
    "IDP": ["integer", 1, f"{project_table}(IDP)"],
    "Title": ["text", 0],
    "StartingDate": ["integer", 0],
    "Employees": [employeelist2_table + "[]", 0],
}
for key, values in tables_dic.items():
    postgresSQLManager.init_table(key, values["table"])

'''
Data Initialization
'''
#  Employee
employees = {} 
for i in range(100):
    employees[i] = {} 
    employees[i] = {
        "IDE": i,
        "Name": f"'Name{i}'",
        "Address": f"'Address{i}'",
        "Age": random.randint(20, 65),
        "Position": f"'Position{i}'",
        "WagesPerHour": random.randint(15, 200),
    }
for employee_id, value in employees.items(): 
    tables_dic[employee_table]["data"].append({
        "IDE": employee_id,
        "Name": value["Name"],
        "Address": value["Address"],
        "Age": value["Age"],
        "Position": value["Position"],
        "WagesPerHour": value["WagesPerHour"],
    })
# Project
projects = {}
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 12, 30)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
for i in range(100):
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    projects[i] = {}
    projects[i] = {
        "Title": f"'Title{i}'",
        "StartingDate": f"'{random_date}'",
    }
for project_id, value in projects.items():
    tables_dic[project_table]["data"].append({
        "IDP": project_id,
        "Title": value["Title"],
        "StartingDate": value["StartingDate"],
    })
# Assignment1
employees_assignments = {}
for employee_id, value in employees.items():
    employees_assignments[employee_id] = []
    random_assignments = random.sample(projects.items(), random.randint(1, len(projects)))
    for i in range(0, len(random_assignments)):
        assignment = random_assignments[i][1]
        assignment["IDP"] = random_assignments[i][0]
        assignment["NumberOfHours"] = random.randint(100, 1000)
        employees_assignments[employee_id].append(assignment)
for employee_id, assigned_projects in employees_assignments.items():
    for project in assigned_projects:
        tables_dic[assignment1_table]["data"].append({
            "IDE": employee_id,
            "IDP": project["IDP"],
            "NumberOfHours": project["NumberOfHours"],
        })
for employee_id, assigned_projects in employees_assignments.items():
    for project in assigned_projects:
        tables_dic[assignment2_table]["data"].append({
            "IDE": employee_id,
            "Name": employees[employee_id]["Name"],
            "WagesPerHour": employees[employee_id]["WagesPerHour"],
            "IDP": project["IDP"],
            "Title": projects[project["IDP"]]["Title"],
            "NumberOfHours": project["NumberOfHours"]
        })
for employee_id, assigned_projects in employees_assignments.items():
    assigned_project_string = ""
    for project in assigned_projects:
        assigned_project_string += f"ROW({project['IDP']},{project['NumberOfHours']}),"
    tables_dic[empass1_table]["data"].append({
        "IDE": employee_id,
        "Address": employees[employee_id]["Address"],
        "Age": employees[employee_id]["Age"],
        "Position": employees[employee_id]["Position"],
        "WagesPerHour": employees[employee_id]["WagesPerHour"],
        "AssignedProjects": f"ARRAY[{assigned_project_string[0:-1]}]::" + projectlist1_table + "[]",
    })
for employee_id, assigned_projects in employees_assignments.items():
    assigned_project_string = ""
    for project in assigned_projects:
        assigned_project_string += f"ROW({project['IDP']},{project['Title']},{project['NumberOfHours']}),"
    tables_dic[empass2_table]["data"].append({
        "IDE": employee_id,
        "Name": employees[employee_id]["Name"],
        "Address": employees[employee_id]["Address"],
        "Age": employees[employee_id]["Age"],
        "Position": employees[employee_id]["Position"],
        "WagesPerHour": employees[employee_id]["WagesPerHour"],
        "AssignedProjects": f"ARRAY[{assigned_project_string[0:-1]}]::" + projectlist2_table + "[]",
    })
for key, values in tables_dic.items():
    for value in values["data"]:
        postgresSQLManager.insert_data(key, value)

# Get Data
for key, values in tables_dic.items():
    postgresSQLManager.get_table_data(key)

postgresSQLManager.close()
