import pandas as pd 
import matplotlib.pyplot as plt

budgData = pd.read_csv ('C:\\Users\\Renz\\Pythonprac\\corePython_dataHandling\\simpleDataAnaylzer\\BudgetDataSet.csv')
# always create newline for printing 
print(budgData.to_string())

# calculates the total spending 
total_amount = budgData['Amount'].sum() 
print(f"Total Amount: {total_amount}")

# top spending category 
top_spend = budgData['Category'].mode()[0]
print(f"Top Spending Category: {top_spend}") 

# sets up bar plot for spend per category 
spend_category = budgData.groupby('Category')['Amount'].sum()
spend_category.plot(kind='bar')
plt.title('Total Spend')
plt.xlabel('Category')
plt.ylabel('Total Amount')
plt.tight_layout() # ensures labels dont overlap
plt.show()

# Row with maximum Amount
max_spend = budgData[budgData['Amount'] == budgData ['Amount'].max()]
print(f"Highest Spending Entry: {max_spend}")

# Average amount per category
average_category = budgData.groupby('Category')['Amount'].mean()
print(f"Average Amount per Category: {average_category}")

# Unique Categories
print("All Categories")
print(budgData['Category'].unique())

# Above average spend 
avg_amount = budgData['Amount'].mean()
above_avg = budgData[budgData['Amount'] > avg_amount]

print(f"Entries Above Average Spend: {above_avg}")

# Logic for High Spend 
budgData['Is High Spend'] = budgData['Amount'] > avg_amount 
print(budgData[['Amount' , 'Is High Spend']])


# filter by date 
food_data = budgData[budgData['Category'] == 'Food']
print(food_data)

# save csv file 
food_data.to_csv("filteredbyFood.csv", index=False)