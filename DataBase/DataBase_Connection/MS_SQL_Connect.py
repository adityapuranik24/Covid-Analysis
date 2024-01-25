import pyodbc


def db_connect():
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                        "Server=ASUS-TUF;"
                        "Database=Covid_Analysis;"
                        "Trusted_Connection=yes;",
                        autocommit= True)

    curser = conn.cursor()

    return curser



db_connect()