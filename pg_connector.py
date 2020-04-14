import psycopg2

class PostgreSQLManger():

    conn = psycopg2.connect("dbname=lab4 user=postgres password=password")
    conn.autocommit = True
    cur = conn.cursor()

    def init(self):
        print('1')

    def init_table(self, table1, fields_dic): # Drop and create table
        self.drop_table(table1)
        self.create_table(table1, fields_dic)

    def drop_table(self, table1):
        self.cur.execute(f"DROP TABLE IF EXISTS {table1}")

    def create_table(self, table1, fields_dic):
        sql = f"CREATE TABLE {table1}("
        fields = ""
        primary_key = []
        for key, value in fields_dic.items():
            if value[1]:
                primary_key.append(key)
            fields += f"{key} {value[0]},"
        if len(primary_key) > 0:
            primary_key_string = ', '.join(primary_key)
            sql += fields + "PRIMARY KEY (" + primary_key_string
            sql = sql + "))"
            self.cur.execute(sql)
        else:
            self.cur.execute(sql + fields[:-1] + ")")

    def insert_data(self, table1, data_dic):
        sql = f"INSERT INTO {table1} ("
        for key in data_dic.keys():
            sql += f"{key},"
        sql = sql[0: -1] +  ") VALUES ("
        for value in data_dic.values():
            sql += f"{value},"
        sql = sql[0: -1] + ");"
        self.cur.execute(sql)


    def get_table_data(self, table1):
        self.cur.execute(f"SELECT * from {table1}")
        rows = self.cur.fetchall()
        print(f"Table: {table1}")
        for row in rows:
            print(row)
    
    def print_cur(self):
        print(self.cur)
    
    def close(self):
        self.conn.close()


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
data_dic = {}
data_dic["IDE"] = 1
data_dic["Name"] = "'Enoch'"
data_dic["WagesPerHour"] = 25
data_dic["IDP"] = 1
data_dic["Title"] = "'Title'"
data_dic["NumberOfHours"] = 10
postgresSQLManager.insert_data(table1, data_dic)

data_dic2 = {}
data_dic2["IDP"] = 1
data_dic2["NumberOfHours"] = 10
postgresSQLManager.insert_data(table2, data_dic2)

data_dic3 = {
    "IDE": 1,
    "Address": "'Diamond Bar'",
    "Age": 30,
    "Position": "'Manager'",
    "WagesPerHour": 45,
    "AssignedProjects": "ARRAY[ROW(1, 10), ROW(2, 15)]::" + table2 + "[]",
}
postgresSQLManager.insert_data(table3, data_dic3)

# Get Data
postgresSQLManager.get_table_data(table1)
postgresSQLManager.get_table_data(table2)
postgresSQLManager.get_table_data(table3)

postgresSQLManager.print_cur()
postgresSQLManager.close()
