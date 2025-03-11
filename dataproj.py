#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[36]:


# the csv file used "," due to which the data was unreadable so the delimiter was used to remove ";"
df = pd.read_csv("student-mat.csv", delimiter=";")


# In[37]:


# Displaying the first few rows
print(df.head())


# In[102]:


print("Missing values:\n",df.isnull().sum())


# In[99]:


print("\nData Types:\n", df.dtypes)


# In[101]:


print("Dataset Size:", df.shape)


# In[40]:


missing_values = df.isnull().sum().sum()
print(f"Total missing values: {missing_values}")


# In[41]:


# If missing values found.
# Handle missing values (replace with median)
df.fillna(df.median(numeric_only=True), inplace=True)


# In[42]:


duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")


# In[43]:


# If duplicate values found
# Remove duplicates
df.drop_duplicates(inplace=True)


# In[45]:


# 1. What is the average score in math (G3)?
avg_math_score = df['G3'].mean()
print(f"The average score in math (G3) is: {avg_math_score:.2f}")


# In[46]:


# 2. How many students scored above 15 in their final grade (G3)?
students_above_15 = df[df['G3'] > 15].shape[0]
percentage_above_15 = (students_above_15 / df.shape[0]) * 100
print(f"Number of students who scored above 15 in G3: {students_above_15}")
print(f"Percentage of students who scored above 15 in G3: {percentage_above_15:.2f}%")


# In[49]:


# 3. Is there a correlation between study time (studytime) and the final grade (G3)?
correlation = df['studytime'].corr(df['G3'])
print(f"Correlation between study time and final grade (G3): {correlation:.4f}")
# Interpreting the correlation
if abs(correlation) < 0.3:
    interpretation = "weak"
elif abs(correlation) < 0.7:
    interpretation = "moderate"
else:
    interpretation = "strong"

direction = "positive" if correlation > 0 else "negative"
if abs(correlation) < 0.01:
    conclusion = "There is almost no correlation between study time and final grade."
else:
    conclusion = f"There is a {interpretation} {direction} correlation between study time and final grade."

print(conclusion)


# In[57]:


## 4. Which gender has a higher average final grade (G3)?
avg_by_gender = df.groupby('sex')['G3'].mean().round(2)
print("Average final grade (G3) by gender:")
print(avg_by_gender)

if avg_by_gender['F'] > avg_by_gender['M']:
    print("Female students have a higher average final grade.")
elif avg_by_gender['M'] > avg_by_gender['F']:
    print("Male students have a higher average final grade.")
else:
    print("Both genders have the same average final grade.")


# In[71]:


# 1. Plot a histogram of final grades (G3)
plt.figure(figsize=(10, 6))
sns.histplot(df['G3'], bins=20, kde=True)
plt.title('Distribution of Final Grades (G3)')
plt.xlabel('Final Grade')
plt.ylabel('Number of Students')
plt.grid(True, alpha=0.3)
plt.savefig('g3_histogram.png')


# In[85]:


# 2. Create a scatter plot between study time (studytime) and final grade (G3)
plt.figure(figsize=(10, 6))
plt.scatter(df['studytime'], df['G3'], alpha=0.6)
plt.title('Relationship Between Study Time and Final Grade')
plt.xlabel('Study Time (weekly hours)')
plt.ylabel('Final Grade (G3)')
plt.grid(True, alpha=0.3)

# Adding a best fit line
x = df['studytime']
y = df['G3']
m, b = np.polyfit(x, y, 1)  # m=slope, b=intercept
plt.plot(x, m*x + b, color='red', linestyle='--')

# Add correlation coefficient to the plot
correlation = df['studytime'].corr(df['G3'])
plt.text(0.05, 0.15, f"Correlation: {correlation:.2f}", 
         transform=plt.gca().transAxes,
         bbox=dict(facecolor='white', alpha=0.5))

plt.savefig('studytime_vs_g3.png')


# In[97]:


# Create a simple bar chart comparing grades by gender
plt.figure(figsize=(10, 6))  # Set the size of the plot (width, height in inches)

# Create a bar chart from our gender data
avg_by_gender.plot(kind='bar', color=['pink', 'red'])

# Add labels and title
plt.title('Average Final Grade by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Final Grade')

# Keep the x-axis labels horizontal (not rotated)
plt.xticks(rotation=0)

# Add grid lines (only horizontal ones)
plt.grid(axis='y',alpha= 0.3)

# Put the actual values on top of each bar
for i, value in enumerate(avg_by_gender):
    plt.text(i, value + 0.1, f"{value:.2f}", 
             horizontalalignment='center', 
             fontweight='bold')

# Save and show the plot
plt.savefig('gender_comparison.png')


# In[ ]:




