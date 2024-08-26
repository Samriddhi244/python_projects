import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load the datasets from the provided Excel files
girlsvillage_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\girls village.xlsx')
boysvillage_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\boysvillage.xlsx')
girlscity_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\girlscity.xlsx')
boyscity_data = pd.read_excel(r'C:\Users\ASUS\OneDrive\Desktop\boyscity.xlsx')

# Display the first few rows of each dataset to understand their structure
print(girlsvillage_data.head())
print(boysvillage_data.head())
print(boyscity_data.head())
print(girlscity_data.head())
# Add Gender column to each dataset
girlsvillage_data['Gender'] = 'Girl'
boysvillage_data['Gender'] = 'Boy'
girlscity_data['Gender'] = 'Girl'
boyscity_data['Gender'] = 'Boy'
girlsvillage_data['Area'] = 'village'
boysvillage_data['Area'] = 'village'
girlscity_data['Area'] = 'city'
boyscity_data['Area'] = 'city'


# Combine the datasets
combined_data = pd.concat([girlsvillage_data, boysvillage_data, girlscity_data, boyscity_data], ignore_index=True)

# Display the first few rows of the combined dataset
combined_data.head()

# Define the formula for the ANOVA model
formula = 'TOTAL ~ C(TOTAL) * C(Gender) * C(Area)'

# Fit the model
model = ols(formula, data=combined_data).fit()

# Perform the ANOVA
anova_table = sm.stats.anova_lm(model, typ=2)

# Display the ANOVA table
print(anova_table)

