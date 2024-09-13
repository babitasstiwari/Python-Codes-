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
CREATE TABLE BT_agents (
    agent_code VARCHAR(100) NOT NULL PRIMARY KEY, 
    agent_name VARCHAR(100) NOT NULL,
    working_area VARCHAR(100) NOT NULL,
    commission VARCHAR(100) NOT NULL,
    phone_no VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL
);
""")

# Insert data into the table
cursor.execute("""
INSERT INTO BT_agents(agent_code, agent_name, working_area, commission, phone_no, country)
VALUES 
('A007', 'Ramasundar', 'Bangalore', '0.15', '077-25814763', 'India'),
('A003', 'Alex', 'London', '0.13', '075-12458969', 'USA'),
('A008', 'Alford', 'New York', '0.12', '044-25874365', 'USA'),
('A011', 'Ravi Kumar', 'Bangalore', '0.15', '077-45625874', 'India'),
('A010', 'Santakumar', 'Chennai', '0.14', '007-22388644', 'Canada'),
('A012', 'Lucida', 'San Jose', '0.12', '044-52981425', 'USA'),
('A005', 'Anderson', 'Brisban', '0.13', '045-21447739', 'Australia'),
('A001', 'Subbarao', 'Bangalore', '0.14', '077-12346674', 'India'),
('A002', 'Mukesh', 'Mumbai', '0.11', '029-12358964', 'India'),
('A006', 'McDen', 'London', '0.15', '078-22255588', 'United Kingdom');
""")

myconn.commit()

# Read data from the table
query = "SELECT * FROM BT_agents"
df = pd.read_sql(query, myconn)
print(df)

# Close the cursor and connection
cursor.close()
myconn.close()