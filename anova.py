import pandas as pd

# Load the datasets from the provided Excel files
girlsvillage_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\girls village.xlsx')
boysvillage_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\boysvillage.xlsx')
girlscity_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\girlscity.xlsx')
boyscity_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\boyscity.xlsx')

# Display the first few rows of each dataset to understand their structure
girlsvillage_data.head(), boysvillage_data.head(), boyscity_data.head(), girlscity_data.head()
