import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Extract data from CSV

starbucks = "/Users/nominnemo/Desktop/Python tasks/Python Assignment/starbucks.csv"
df = pd.read_csv(starbucks)

# Change the type of Caffeine into numbers and make the 'Varies' to O 
df['Caffeine (mg)'] = pd.to_numeric(df['Caffeine (mg)'], errors='coerce').fillna(0)


# Load it into Snowflake 
conn = snowflake.connector.connect (
    user= "NOMINERDENE",
    password= '*****',
    account= "FHNWFWN-OT79270",
    database= "Python",
    schema= "Assessment"
)


write_pandas(conn, df, "movies", auto_create_table=True)
