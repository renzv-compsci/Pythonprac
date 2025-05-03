import pandas as pd 
import matplotlib as pld 

budgData = pd.read_csv ('C:\\Users\\Renz\\Pythonprac\\corePython_dataHandling\\simpleDataAnaylzer\\BudgetDataSet.csv')
# always create newline for printing 
print(budgData.to_string())

# calculates the total spending 

total_amount = budgData['Amount'].sum() 
print(f"Total Amount: {total_amount}")

# top spending category 
top_spend = budgData['Category'].mode()[0]
print(f"Top Spending Category: {top_spend}") 

# returns all categories that ties with max spends
