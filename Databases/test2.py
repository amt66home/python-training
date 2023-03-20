import pandas as pd
import pyodbc 
cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-A81D72E\SQL2019,1433;DATABASE=dba;\Trusted_Connection=yes;')
df = pd.read_sql_query('select TOP 10 * from dbo.myTable', cnxn)
df.head()


cnxn = pyodbc.connect('Driver={SQL Server};Server=.;DATABASE=dba;\Trusted_Connection=yes;')


cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT * from myTable;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()


