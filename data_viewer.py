from pg_manager import PostgreSQLManger

postgresSQLManager = PostgreSQLManger()
postgresSQLManager.query_selector("SELECT WagesPerHour * NumberOfHours FROM Assignment2")
postgresSQLManager.query_selector("SELECT AssignedProjects FROM EmpAss1")