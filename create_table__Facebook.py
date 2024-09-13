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
CREATE TABLE BT_Facebook (
    user_id VARCHAR(100) NOT NULL,
    post_id VARCHAR(100) NOT NULL,
    post_date DATETIME NOT NULL,
    post_content VARCHAR(100) NOT NULL  
);
""")

# Insert data into the table
cursor.execute("""
INSERT INTO BT_Facebook (user_id, post_id, post_date, post_content)
VALUES
('151652', '599415','2021-07-10 12:00:00', 'Need a hug'),
('661093', '624356','2021-07-29 13:00:00', 'Bed. Class. Work. Gym.Then class'),
('004239', '784254','2021-07-04 11:00:00', 'Happy 4th of July!'),
('661093', '442560','2021-07-08 14:00:00', 'Just going to cry myself to sleep after watching Marley and Me.'),
('151652', '111766', '2021-07-12 19:00:00', 'I am so done with covid need travelling ASAP!')
""")

myconn.commit()

# Read data from the table
query = "SELECT * FROM BT_Facebook"
df = pd.read_sql(query, myconn)
print(df)

# Close the cursor and connection
cursor.close()
myconn.close()