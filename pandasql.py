import pandas as pd
import pandasql as psql

# Read the Excel file into a DataFrame
excel_file_path = "/home/akhil/Downloads/demo-sample.xlsx"
df = pd.read_excel(excel_file_path, sheet_name='Sheet1')  # Change 'Sheet1' to your sheet name if needed

# Define your SQL query
query = """
SELECT *
FROM df
limit 10
"""  # Modify this query as per your requirement

# Execute the query
result = psql.sqldf(query, locals())

# Display the result
print(result)