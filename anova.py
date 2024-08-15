import pandas as pd

# Load the datasets from the provided Excel files
girlsvillage_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\girls village.xlsx')
boysvillage_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\boysvillage.xlsx')
girlscity_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\girlscity.xlsx')
boyscity_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\boyscity.xlsx')

# Display the first few rows of each dataset to understand their structure
girlsvillage_data.head(), boysvillage_data.head(), boyscity_data.head(), girlscity_data.head()
# Add Gender column to each dataset
girlsvillage_data['Gender'] = 'Girl'
boysvillage_data['Gender'] = 'Boy'
girlscity_data['Gender'] = 'Girl'
boyscity_data['Gender'] = 'Boy'

# Combine the datasets
combined_data = pd.concat([girlsvillage_data, boysvillage_data, girlscity_data, boyscity_data], ignore_index=True)

# Display the first few rows of the combined dataset
combined_data.head()
