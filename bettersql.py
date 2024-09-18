import pandas as pd
from bettersql import sql

# Read the Excel file into a DataFrame
excel_file_path = "/home/akhil/Downloads/MreDepot2024MarginProdhubUpload - Sheet1 (2).csv"
df = pd.read_csv(excel_file_path)  # Change 'Sheet1' to your sheet name if needed

# Define your SQL query
query = """
SELECT *
FROM df
limit 10
"""  # Modify this query as per your requirement

# Execute the query using bettersql
result = sql(query, df)

# Display the result
print(result)
