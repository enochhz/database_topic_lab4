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
        print(f"===== {table1} =====")
        for row in rows:
            print(row)
    
    def query_selector(self, sql_query):
        self.cur.execute(sql_query)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
    
    def print_cur(self):
        print(self.cur)
    
    def close(self):
        self.conn.close()
