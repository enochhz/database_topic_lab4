from pg_manager import PostgreSQLManger
import time

postgresSQLManager = PostgreSQLManger()
def query_runner(query_name, sql_query):
    print(f"===== {query_name} =====")
    start_time = time.time()
    postgresSQLManager.run_query(sql_query)
    print(f"Run time(seconds): {time.time() - start_time}")

query_runner("query1", "SELECT Employee.IDE, SUM(Assignment1.NumberOfHours) * WagesPerHour " + 
            "FROM Employee LEFT JOIN Assignment1 ON  Employee.IDE = Assignment1.IDE Group By Employee.IDE, Employee.Name, Employee.WagesPerHour"); 
query_runner("query2", "SELECT IDE, SUM(NumberOfHours) * WagesPerHour " + 
            "FROM (SELECT IDE, WagesPerHour, (unnest(AssignedProjects)::ProjectList1).NumberOfHours FROM EmpAss1) As EmpAss " + 
            "GROUP BY IDE, WagesPerHour")

query_runner("query3", "SELECT IDE, Name, SUM(NumberOfHours) * WagesPerHour " + 
            "FROM (SELECT IDE, Name, WagesPerHour, (unnest(AssignedProjects)::ProjectList2).NumberOfHours FROM EmpAss2) As EmpAss " +
            "GROUP BY IDE, Name, WagesPerHour")
query_runner("query4", "SELECT IDE, Name, SUM(Assignment2.NumberOfHours) * WagesPerHour FROM Assignment2 Group By IDE, Name, WagesPerHour"); 

query_runner("query5", "SELECT Employee.IDE, Employee.Name, Project.IDP, Project.Title, Employee.WagesPerHour * Assignment1.NumberOfHours " + 
            "FROM Employee LEFT JOIN Assignment1 INNER JOIN Project ON Assignment1.IDP = Project.IDP ON Assignment1.IDE = Employee.IDE " +
            "GROUP BY Employee.IDE, Project.IDP, Assignment1.NumberOfHours" )
query_runner("query6", "SELECT IDE, Name, IDP, Title, WagesPerHour * NumberOfHours " + 
            "FROM Assignment2 GROUP BY IDE, IDP")

query_runner("query7", "SELECT IDE, Name, IDP, Title, SUM(NumberOfHours) * WagesPerHour " + 
            "FROM (SELECT IDE, Name, WagesPerHour, " + 
            "(unnest(AssignedProjects)::ProjectList2).IDP, (unnest(AssignedProjects)::ProjectList2).Title, (unnest(AssignedProjects)::ProjectList2).NumberOfHours FROM EmpAss2) As EmpAss " + 
            "GROUP BY IDE, Name, IDP, Title, WagesPerHour")
query_runner("query8", "SELECT Employee.IDE, Employee.Name, EmpAss.IDP, Project.Title, SUM(EmpAss.NumberOfHours) * Employee.WagesPerHour " + 
            "FROM Employee LEFT JOIN (SELECT IDE, WagesPerHour, (unnest(AssignedProjects)::ProjectList1).IDP, (unnest(AssignedProjects)::ProjectList1).NumberOfHours FROM EmpAss1) As EmpAss " + 
            "INNER JOIN Project ON EmpAss.IDP = Project.IDP ON Employee.IDE = EmpAss.IDE " + 
            "GROUP BY Employee.IDE, Employee.WagesPerHour, EmpAss.IDP, Project.Title")