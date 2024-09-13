import mysql.connector
import pandas as pd

myconn = mysql.connector.connect(
    user='user',
    password='yourpassword',
    host='hostlink',
    database='schema_name')

cursor = myconn.cursor()

cursor.execute("""
CREATE TABLE BT_Traders (
    order_id VARCHAR(100) NOT NULL PRIMARY KEY,
    user_id VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    status VARCHAR(100) NOT NULL,
    timestamp DATETIME NOT NULL
);
""")

cursor.execute("""
INSERT INTO BT_Traders (order_id, user_id, price, quantity, status, timestamp)
VALUES
('100101', '111', 9.80, 10, 'Cancelled', '2022-08-17 12:00:00'),
('100102', '111', 10.00, 10, 'Completed', '2022-08-17 12:00:00'),
('100259', '148', 5.10, 35, 'Completed', '2022-08-25 12:00:00'),
('100264', '148', 4.80, 40, 'Completed', '2022-08-26 12:00:00'),
('100305', '300', 10.00, 15, 'Completed', '2022-09-05 12:00:00'),
('100400', '178', 9.90, 15, 'Completed', '2022-09-09 12:00:00'),
('100565', '265', 25.60, 5, 'Completed', '2022-12-19 12:00:00');
""")

query = "SELECT * FROM BT_Traders"
df = pd.read_sql(query, myconn)
df