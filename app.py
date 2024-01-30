import pyodbc

SERVER = 'MX20-03093\\SQLTEST'
DATABASE = 'warehouse'
USERNAME = 'sa'
PASSWORD = '*******'

print(SERVER)
connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

SQL_QUERY = """ 
SELECT TOP (1000) [Product_Id]
      ,[Name]
      ,[Price]
      ,[Description]
  FROM [warehouse].[dbo].[Product] 
  """

SQL_QUERY2 = """ 
SELECT (1000) [Product_Id]
      ,[Name]
      ,[Price]
      ,[Description]
  FROM [warehouse].[dbo].[Product] 
  """

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records: 
    print(f"{r.Product_Id}\t{r.Name}\t{r.Price}\t{r.Description}")

 #example of adding a change    

#branch to edit the queries   