import pyodbc 
import pandas as pd
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'DESKTOP-A81D72E\SQL2019,1433' 
database = 'dba' 
username = 'sectest' 
password = 'Password-01' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)

cnxn = pyodbc.connect("DSN=AMT")
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT * from myTable;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=name;"
                      "Database=database;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
df = pd.read_sql_query('select * from mytable', cnxn)