import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("titanic.csv")

# Shape and Basic Info
print("Dataset Shape:", df.shape)
print("\nColumn Info:")
print(df.info())
print("\nFirst 5 Rows:\n", df.head())

# Summary Statistics
print("\nDescriptive Statistics:\n", df.describe(include='all'))

# Missing Values
print("\nMissing Values:\n", df.isnull().sum())

# Handling Missing Values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)

# Histograms
for col in ['Age', 'Fare']:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True, color='skyblue')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Boxplots
for col in ['Age', 'Fare']:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col], color='orange')
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()

# Correlation Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# Pairplot
sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare']], hue='Survived', palette='husl')
plt.show()

# Categorical Countplots
for col in ['Sex', 'Embarked', 'Pclass']:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x=col, hue='Survived', palette='Set2')
    plt.title(f'Survival Count by {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

# Pie Chart for Survival Rate
survived_counts = df['Survived'].value_counts()
labels = ['Not Survived', 'Survived']
colors = ['#ff9999', '#66b3ff']
plt.figure(figsize=(5, 5))
plt.pie(survived_counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Survival Rate')
plt.tight_layout()
plt.show()

# Age vs Survived Boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x='Survived', y='Age', data=df, palette='pastel')
plt.title('Age Distribution by Survival')
plt.xlabel('Survived')
plt.ylabel('Age')
plt.tight_layout()
plt.show()

# Final Summary of Insights
print("\nInsights:")
print("- Females had significantly higher survival rates.")
print("- Passengers from higher classes (Pclass 1) were more likely to survive.")
print("- Age and Fare have some outliers, especially Fare.")
print("- Younger passengers had a better chance of survival.")
print("- Embarked location and Sex are key factors in survival prediction.")
