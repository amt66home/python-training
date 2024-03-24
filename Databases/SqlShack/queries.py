import pyodbc

DBInstance = 'DESKTOP-A81D72E\SQL2019'
DB = 'SQLShackDemo'
username = 'sectest'
password = 'EAzM3Cf6rq5csi'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+DBInstance+';DATABASE='+DB+';ENCRYPT=no;UID='+username+';PWD='+ password)

cursor_1 = cnxn.cursor()

tsql = """
SELECT
    @@SERVERNAME as serverName,
    database_id,
    CONVERT(VARCHAR(25), DB.name) AS dbName,
    CONVERT(VARCHAR(10), DATABASEPRPERTYEX(name, 'status')) AS [Status],
    state_desc,
    (SELECT COUNT(1) FROM sys.master_fiels WHERE DB_NAME(database_id) = DB.name AND type_desc = 'rows') AS DataFiles,
    (SELECT COUNT(1) FROM sys.master_files WHERE DB_NAME(database_id) = DB.name AND type_desc = 'log') AS LogFiles,
    (SELECT SUM((size*8)/1024) FROM sys.master_files WHERE DB_NAME(database_id) = DB.name AND type_desc = 'log') AS [Log MB]),
    user_access_desc AS [User Access],
    recovery_model_desc AS [Recovery Model]
    FROM sys.databases as DB
    ORDER BY dbName;
"""
cursor = cnxn.cursor()
cursor.execute("SELECT @@SERVERNAME as serverName, database_id, CONVERT(VARCHAR(25), DB.name) AS dbName, CONVERT(VARCHAR(10), DATABASEPRPERTYEX(name, 'status')) AS [Status], state_desc,    (SELECT COUNT(1) FROM sys.master_fiels WHERE DB_NAME(database_id) = DB.name AND type_desc = 'rows') AS DataFiles,    (SELECT COUNT(1) FROM sys.master_files WHERE DB_NAME(database_id) = DB.name AND type_desc = 'log') AS LogFiles,    (SELECT SUM((size*8)/1024) FROM sys.master_files WHERE DB_NAME(database_id) = DB.name AND type_desc = 'log') AS [Log MB]),    user_access_desc AS [User Access],    recovery_model_desc AS [Recovery Model]    FROM sys.databases as DB    ORDER BY dbName;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()