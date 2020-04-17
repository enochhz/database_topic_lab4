from pg_manager import PostgreSQLManger

postgresSQLManager = PostgreSQLManger()

#postgresSQLManager.query_selector("SELECT WagesPerHour * NumberOfHours FROM Assignment2")
#postgresSQLManager.query_selector("SELECT AssignedProjects FROM EmpAss1")
#postgresSQLManager.query_selector("SELECT * FROM ProjectList1 WHERE IDP IN (SELECT AssignedProjects[1].IDP FROM EmpAss1)")
#postgresSQLManager.query_selector("SELECT AssignedProjects[2].IDP FROM EmpAss1")
#postgresSQLManager.query_selector("SELECT AssignedProjects FROM EmpAss1")
#postgresSQLManager.query_selector("SELECT unnest(AssignedProjects) FROM EmpAss1")
#postgresSQLManager.query_selector("SELECT SUM(NumberOfHours) FROM ProjectList1 WHERE IDP IN (SELECT (unnest(AssignedProjects)::ProjectList1).IDP FROM EmpAss1)")
#print("===== test1 =====")
#postgresSQLManager.query_selector("SELECT (unnest(AssignedProjects)::ProjectList1).NumberOfHours FROM EmpAss1")
#print("===== sum of type array =====")
#postgresSQLManager.query_selector("SELECT SUM(NumberOfHours) FROM (SELECT (unnest(AssignedProjects)::ProjectList1).NumberOfHours FROM EmpAss1) AS ProjectLists")
print("===== query3 =====")
postgresSQLManager.query_selector("SELECT Emp.Name, SUM(NumberOfHours) * Emp.WagesPerHour " + 
                                  "FROM Employee Emp LEFT JOIN (SELECT IDE, (unnest(AssignedProjects)::ProjectList2).NumberOfHours FROM EmpAss2) As EmpAss ON Emp.IDE = EmpAss.IDE " +
                                  "GROUP BY Emp.IDE")