import pyodbc


conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=ASUS-TUF;"
                      "Database=Covid Analysis;"
                      "Trusted_Connection=yes;")


curser = conn.cursor()
# data = curser.execute("select * from dbo.EMPLOYEE;")
# for row in data:
#     print(row)