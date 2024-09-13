import mysql.connector
import pandas as pd
import os
import matplotlib.pyplot as plt

# Creating MySQL connection to the database.
myconn = mysql.connector.connect
cursor = myconn.cursor()

# Assigning a directory path.
loc = 'ex_files'

paths = os.listdir(path=loc)
print(paths)
for file in paths:
    if file.endswith(".xlsx"):
        print(file)

        # Get the table name from the file name
        table_name = file.split(".")[0]

        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(f"{loc}/{file}")

        # Create a new table for this DataFrame
        query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ("
        for column_name in df.columns:
            column_name = column_name.strip()
            query += f" `{column_name}` VARCHAR(100),"
        query = f"{query[:-1]});"
        print(query)
        cursor.execute(query)

        # Insert data into the table
        insert_data_base = f"INSERT INTO `{table_name}` ({', '.join([f'`{col.strip()}`' for col in df.columns])}) VALUES"
        for index, row in df.iterrows():
            values = ', '.join(['%s' for _ in range(len(row))])
            insert_data = f"{insert_data_base} ({values})"
            print(insert_data)
            cursor.execute(insert_data, tuple(row))

myconn.commit()
    
# Joining the tables. 
query = """
CREATE TABLE IF NOT EXISTS `EnergyConsumption_details` AS
SELECT * FROM `EnergyConsumption2020`
UNION ALL
SELECT * FROM `EnergyConsumption2021`
UNION ALL
SELECT * FROM `EnergyConsumption2022`
UNION ALL
SELECT * FROM `EnergyConsumption2023`
"""
cursor.execute(query)

#Fetching the data
sql_vz = "SELECT * FROM EnergyConsumption_details"
cursor.execute(sql_vz)
data_vz = cursor.fetchall()

columns = [i[0] for i in cursor.description]
df = pd.DataFrame(data_vz, columns=columns)

myconn.commit()
cursor.close()

df['electricty_usage'] = pd.to_numeric(df['electricty_usage'], errors='coerce')

#grouping the data by year
grouped_df = df.groupby('year')['electricty_usage'].sum()

# plotting the data 
plt.figure(figsize=(12, 6))
grouped_df.plot(kind='bar', stacked= True)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Energy Consumption Details')
plt.legend(['Electricity Usage'])
plt.show()









