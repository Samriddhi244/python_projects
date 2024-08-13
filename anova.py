import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load the Excel file
file_path = r'C:\Users\ASUS\OneDrive\Desktop\boyscity.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows to understand the structure
print(data.head())

# Replace 'DependentVariable' and 'IndependentVariable' with the actual column names from your data
dependent_variable = 'MB6'
independent_variable = 'STRESS'

# Build the ANOVA model
model = ols(f'{dependent_variable} ~ C({independent_variable})', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Print the ANOVA table
print(anova_table)

# Check assumptions: Normality and Homogeneity of variance
# Normality check (Shapiro-Wilk Test)
w, p_value = stats.shapiro(model.resid)
print(f'Shapiro-Wilk Test: W={w}, p-value={p_value}')

# Homogeneity of variance (Levene's Test)
levene_stat, levene_p_value = stats.levene(*[data[data[independent_variable] == group][dependent_variable] for group in data[independent_variable].unique()])
print(f'Levene\'s Test: Statistic={levene_stat}, p-value={levene_p_value}')
