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
CREATE TABLE BT_microsoft (
    message_id VARCHAR(100) NOT NULL PRIMARY KEY,
    sender_id VARCHAR(100) NOT NULL,
    receiver_id VARCHAR(100) NOT NULL,
    sent_date DATETIME NOT NULL,
    content VARCHAR(100) NOT NULL 
);
""")

# Insert data into the table
cursor.execute("""
INSERT INTO BT_microsoft (message_id, sender_id, receiver_id, sent_date, content)
VALUES
('901', '3601', '4500', '2022-08-03 00:00:00', 'You up!'),
('902', '4500', '3601', '2022-08-03 00:00:00', 'Only if you are buying'),
('743', '3601', '8752', '2022-06-14 00:00:00', 'Let us take this offline'),
('922', '3601', '4500', '2022-08-10 00:00:00', 'Get on the call')
""")

myconn.commit()

# Read data from the table
query = "SELECT * FROM BT_microsoft"
df = pd.read_sql(query, myconn)
print(df)

# Close the cursor and connection
cursor.close()
myconn.close()
