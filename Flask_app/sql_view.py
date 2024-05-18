
# import pandas as pd
# import pyodbc

# server = 'root'
# db = 'studentdb'

# conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')

# sql = """

# SELECT * FROM school_pcm

# """
# df = pd.read_sql(sql, conn)




import pandas as pd
import pyodbc

# Database connection details
server = 'localhost'
db = 'studentdb'
user = 'root'
password = 'Vitm@0858'

# Create the connection string
conn_str = (
    'DRIVER={SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + db + ';'
    'UID=' + user + ';'
    'PWD=' + password + ';'
)

# Connect to the database
conn = pyodbc.connect(conn_str)

# SQL query
sql = """
SELECT * FROM school_pcm
"""

# Execute the query and load the data into a DataFrame
df = pd.read_sql(sql, conn)

# Close the connection
conn.close()

# Display the DataFrame
print(df)
