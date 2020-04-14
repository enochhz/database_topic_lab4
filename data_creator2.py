from pg_manager import PostgreSQLManger

# Database Initialization
postgresSQLManager = PostgreSQLManger()

# Drop all tables_dic
employee_table = "Employee"
project_table = "Project"
assignment1_table = "Assignment1"
assignment2_table = "Assignment2"
table2 = "ProjectList1"
table3 = "EmpAss1"
tables = [employee_table, project_table, assignment2_table, table2, table3, assignment1_table]
tables_dic = {}
for table in tables:
    tables_dic[table] = {"table": None, "data": []}

# for key in tables_dic.keys():
postgresSQLManager.drop_table(table3)
postgresSQLManager.drop_table(table2)
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
tables_dic[table2]["table"] = {
    "IDP": ["integer", 1],
    "NumberOfHours": ["integer", 1]
}
tables_dic[table3]["table"] = {
    "IDE": ["integer", 1],
    "Address": ["text", 0],
    "Age": ["integer", 0],
    "Position": ["text", 0],
    "WagesPerHour": ["integer", 0],
    "AssignedProjects": [table2 + "[]", 0],
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
tables_dic[assignment2_table]["data"].append({
    "IDE": 1,
    "Name": "'Enoch'",
    "WagesPerHour": 25,
    "IDP": 1,
    "Title": "'Title'",
    "NumberOfHours": 10
})
tables_dic[table2]["data"].append({
    "IDP": 1,
    "NumberOfHours": 10
})
tables_dic[table3]["data"].append({
    "IDE": 1,
    "Address": "'Diamond Bar'",
    "Age": 30,
    "Position": "'Manager'",
    "WagesPerHour": 45,
    "AssignedProjects": "ARRAY[ROW(1, 10), ROW(3, 15)]::" + table2 + "[]",
})
for key, values in tables_dic.items():
    for value in values["data"]:
        postgresSQLManager.insert_data(key, value)

# Get Data
for key, values in tables_dic.items():
    postgresSQLManager.get_table_data(key)

postgresSQLManager.print_cur()
postgresSQLManager.close()
