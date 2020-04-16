from pg_manager import PostgreSQLManger

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
postgresSQLManager.drop_table(employee_table)
postgresSQLManager.drop_table(project_table)
postgresSQLManager.drop_table(assignment1_table)
postgresSQLManager.drop_table(assignment2_table)

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
    "StartingDate": ["integer", 0],
}
tables_dic[assignment1_table]["table"] = {
    "IDE": ["integer", 1],
    "IDP": ["integer", 1],
    "NumberOfHours": ["integer", 0],
}
tables_dic[assignment2_table]["table"] = {
    "IDE": ["integer", 1],
    "Name": ["text", 0],
    "WagesPerHour": ["integer", 0],
    "IDP": ["integer", 1],
    "Title": ["text", 0],
    "NumberOfHours": ["integer", 0],
}
tables_dic[projectlist1_table]["table"] = {
    "IDP": ["integer", 1],
    "NumberOfHours": ["integer", 1]
}
tables_dic[projectlist2_table]["table"] = {
    "IDP": ["integer", 0],
    "Title": ["text", 0],
    "NumberOfHours": ["integer", 0]
}
tables_dic[employeelist1_table]["table"] = {
    "IDE": ["integer", 0],
    "NumberOfHours": ["integer", 0],
    "WagesPerHour": ["integer", 0]
}
tables_dic[employeelist2_table]["table"] = {
    "IDE": ["integer", 0],
    "Name": ["text", 0],
    "NumberOfHours": ["integer", 0],
    "WagesPerHour": ["integer", 0]
}
tables_dic[empass1_table]["table"] = {
    "IDE": ["integer", 1],
    "Address": ["text", 0],
    "Age": ["integer", 0],
    "Position": ["text", 0],
    "WagesPerHour": ["integer", 0],
    "AssignedProjects": [projectlist1_table + "[]", 0],
}
tables_dic[empass2_table]["table"] = {
    "IDE": ["integer", 1],
    "Name": ["text", 0],
    "Address": ["text", 0],
    "Age": ["integer", 0],
    "Position": ["text", 0],
    "WagesPerHour": ["integer", 0],
    "AssignedProjects": [projectlist2_table + "[]", 0],
}
tables_dic[projectass1_table]["table"] = {
    "IDE": ["integer", 1],
    "StartingDate": ["integer", 0],
    "Employees": [employeelist1_table + "[]", 0],
}
tables_dic[projectass2_table]["table"] = {
    "IDE": ["integer", 1],
    "Title": ["text", 0],
    "StartingDate": ["integer", 0],
    "Employees": [employeelist2_table + "[]", 0],
}
for key, values in tables_dic.items():
    postgresSQLManager.init_table(key, values["table"])

# Data Initialization
tables_dic[employee_table]["data"].append({
    "IDE": 1,
    "Name": "'Enoch'",
    "Address": "'Diamond Bar'",
    "Age": 25,
    "Position": "'Team Leader'",
    "WagesPerHour": 1000,
})
tables_dic[project_table]["data"].append({
    "IDP": 1,
    "Title": "'Bitsplanet'",
    "StartingDate": 1,
})
tables_dic[assignment1_table]["data"].append({
    "IDE": 1,
    "IDP": 1,
    "NumberOfHours": 10
})
tables_dic[assignment2_table]["data"].append({
    "IDE": 1,
    "Name": "'Enoch'",
    "WagesPerHour": 25,
    "IDP": 1,
    "Title": "'Title'",
    "NumberOfHours": 10
})
tables_dic[projectlist1_table]["data"].append({
    "IDP": 1,
    "NumberOfHours": 10
})
tables_dic[projectlist1_table]["data"].append({
    "IDP": 3,
    "NumberOfHours": 15, 
})
tables_dic[projectlist2_table]["data"].append({
    "IDP": 1,
    "Title": "'Bitsplanet'" ,
    "NumberOfHours": 10
})
tables_dic[employeelist1_table]["data"].append({
    "IDE": 1,
    "NumberOfHours": 10,
    "WagesPerHour": 1000, 
})
tables_dic[employeelist2_table]["data"].append({
    "IDE": 1,
    "Name": "'Enoch'",
    "NumberOfHours": 10,
    "WagesPerHour": 1000, 
})
tables_dic[empass1_table]["data"].append({
    "IDE": 1,
    "Address": "'Diamond Bar'",
    "Age": 30,
    "Position": "'Manager'",
    "WagesPerHour": 45,
    "AssignedProjects": "ARRAY[ROW(1, 10), ROW(3, 15)]::" + projectlist1_table + "[]",
})
tables_dic[empass2_table]["data"].append({
    "IDE": 1,
    "Name": "'Enoch'",
    "Address": "'Diamond Bar'",
    "Age": 30,
    "Position": "'Manager'",
    "WagesPerHour": 45,
    "AssignedProjects": "ARRAY[ROW(1, 'Bitsplanet', 10), ROW(3, 'hehe', 15)]::" + projectlist2_table + "[]",
})
tables_dic[projectass1_table]["data"].append({
    "IDE": 1,
    "StartingDate": 1,
    "Employees": "ARRAY[ROW(1, 10, 1000), ROW(3, 15, 500)]::" + employeelist1_table + "[]",
})
tables_dic[projectass2_table]["data"].append({
    "IDE": 3,
    "Title": "'Good'",
    "StartingDate": 1,
    "Employees": "ARRAY[ROW(1, 'Enoch', 10, 1000), ROW(3, 'David', 15, 500)]::" + employeelist2_table + "[]",
})
for key, values in tables_dic.items():
    for value in values["data"]:
        postgresSQLManager.insert_data(key, value)

# Get Data
for key, values in tables_dic.items():
    postgresSQLManager.get_table_data(key)

# postgresSQLManager.print_cur()
postgresSQLManager.close()
