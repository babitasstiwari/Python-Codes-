import mysql.connector
import pandas as pd
import os

# Creating a new connection to the MySQL database.
myconn = mysql.connector.connect(user='BabitaTiwari', password='password', host='localhost', database='project')

cursor = myconn.cursor()

#assigning a directory path. 
loc = "./data/"

# Excel file into directory
paths = os.listdir(path=loc)
print(paths)
for file in paths:
  if file.endswith(".xlsx"):
    print(file)

  table_name = file.split(".")[0]
  print(table_name)

  df = pd.read_excel(f"{loc}/{file}")

# Creating table 
  colm_name = df.columns
  query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
  for column in colm_name:
    query = f"{query} `{column}` VARCHAR(100),"
  query = f"{query[:-1]});"
  print(query)
  cursor.execute(query)


  # Insert data from into table
  Insert_data = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES" 
  for index, row in df.iterrows():
    values = ', '.join([f"'{value}'" for value in row])
    Insert_data += f"({values}), "
  Insert_data = Insert_data[:-2]
  cursor.execute(Insert_data)
  myconn.commit()

