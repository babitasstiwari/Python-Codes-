import mysql.connector
import pandas as pd

myconn = mysql.connector.connect(
    user='user',
    password='yourpassword',
    host='hostlink',
    database='schema_name')

cursor = myconn.cursor()

# Create the table
cursor.execute("""
CREATE TABLE BT_Wayfair (
    transaction_id VARCHAR(100) NOT NULL PRIMARY KEY,
    product_id VARCHAR(100) NOT NULL,
    transaction_date DATETIME NOT NULL,
    spend DECIMAL(10, 2) NOT NULL 
);
""")

# Insert data into the table
cursor.execute("""
INSERT INTO BT_Wayfair (transaction_id, product_id, transaction_date, spend)
VALUES
('1341', '123424','2019-12-31 12:00:00', '1500.60'),
('1423', '123424','2020-12-31 12:00:00', '1000.20'),
('1623', '123424','2021-12-31 12:00:00', '1246.44'),
('1322', '123424','2022-12-31 12:00:00', '2145.32')
""")

myconn.commit()

# Read data from the table
query = "SELECT * FROM BT_Wayfair"
df = pd.read_sql(query, myconn)
print(df)

# Close the cursor and connection
cursor.close()
myconn.close()