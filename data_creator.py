from pg_manager import PostgreSQLManger

# Database Initialization
postgresSQLManager = PostgreSQLManger()

# Drop all tables
table1 = "Assignment2"
table2 = "ProjectList1"
table3 = "EmpAss1"
postgresSQLManager.drop_table(table3)
postgresSQLManager.drop_table(table2)
postgresSQLManager.drop_table(table1)

# Tables Initialization
fields_dic = {}
fields_dic["IDE"] = ["integer", 1]
fields_dic["Name"] = ["text", 0]
fields_dic["WagesPerHour"] = ["integer", 0]
fields_dic["IDP"] = ["integer", 1]
fields_dic["Title"] = ["text", 0]
fields_dic["NumberOfHours"] = ["integer", 0]
postgresSQLManager.drop_table(table1)
postgresSQLManager.create_table(table1, fields_dic)

fields_dic2 = {
    "IDP": ["integer", 1],
    "NumberOfHours": ["integer", 1]
}
postgresSQLManager.init_table(table2, fields_dic2)

fields_dic3 = {
    "IDE": ["integer", 1],
    "Address": ["text", 0],
    "Age": ["integer", 0],
    "Position": ["text", 0],
    "WagesPerHour": ["integer", 0],
    "AssignedProjects": [table2 + "[]", 0],
}
postgresSQLManager.init_table(table3, fields_dic3)

# Data Initialization
data_dic = {
    "IDE": 1,
    "Name": "'Enoch'",
    "WagesPerHour": 25,
    "IDP": 1,
    "Title": "'Title'",
    "NumberOfHours": 10
}
postgresSQLManager.insert_data(table1, data_dic)

data_dic2 = {
    "IDP": 1,
    "NumberOfHours": 10
}
postgresSQLManager.insert_data(table2, data_dic2)

data_dic3 = {
    "IDE": 1,
    "Address": "'Diamond Bar'",
    "Age": 30,
    "Position": "'Manager'",
    "WagesPerHour": 45,
    "AssignedProjects": "ARRAY[ROW(1, 10), ROW(3, 15)]::" + table2 + "[]",
}
postgresSQLManager.insert_data(table3, data_dic3)

# Get Data
postgresSQLManager.get_table_data(table1)
postgresSQLManager.get_table_data(table2)
postgresSQLManager.get_table_data(table3)

postgresSQLManager.print_cur()
postgresSQLManager.close()
