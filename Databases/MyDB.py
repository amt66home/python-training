import pyodbc

server = 'DESKTOP-A81D72E\SQL2019'
database = 'dba'
username = 'sectest'
password = 'Password-01'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)

#Sample select query
cursor = cnxn.cursor()
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()