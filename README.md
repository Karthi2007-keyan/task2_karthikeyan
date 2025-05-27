# task2_karthikeya

# Titanic Dataset - Exploratory Data Analysis (EDA)

This project performs exploratory data analysis on the Titanic dataset using Python libraries like `pandas`, `matplotlib`, and `seaborn`. The goal is to understand the structure, trends, and relationships in the data using summary statistics and visualizations.

---

## 📦 Packages Used

To run this code, ensure the following Python libraries are installed:

```bash
pip install pandas matplotlib seaborn

# OUTPUT

PS D:\karthikeyan_elivatelab>  & 'c:\Users\shiva\AppData\Local\Programs\Python\Python313\python.exe' 'c:\Users\shiva\.vscode\extensions\ms-python.debugpy-2025.8.0-win32-x64\bundled\libs\debugpy\launcher' '50196' '--' 'd:\karthikeyan_elivatelab\task2.py' 
Dataset Shape: (10, 12)

Column Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   PassengerId  10 non-null     int64
 1   Survived     10 non-null     int64
 2   Pclass       10 non-null     int64
 3   Name         10 non-null     object
 4   Sex          10 non-null     object
 5   Age          8 non-null      float64
 6   SibSp        10 non-null     int64
 7   Parch        10 non-null     int64
 8   Ticket       10 non-null     object
 9   Fare         10 non-null     float64
 10  Cabin        4 non-null      object
 11  Embarked     10 non-null     object
dtypes: float64(2), int64(5), object(5)
memory usage: 1.1+ KB
None

First 5 Rows:
    PassengerId  Survived  Pclass      Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3     karth    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1            2         1       1    ananya  female  38.0      1      0          PC 17599  71.2833   C85        C
2            3         1       3  saipriya  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3            4         1       1   srilaka  female  35.0      1      0            113803  53.1000  C123        S
4            5         0       3      toji    male   NaN      0      0            373450   8.0500   NaN        S

Descriptive Statistics:
         PassengerId   Survived     Pclass   Name   Sex        Age      SibSp      Parch     Ticket       Fare Cabin Embarked
count      10.00000  10.000000  10.000000     10    10   8.000000  10.000000  10.000000         10  10.000000     4       10
unique          NaN        NaN        NaN     10     2        NaN        NaN        NaN         10        NaN     4        3
top             NaN        NaN        NaN  karth  male        NaN        NaN        NaN  A/5 21171        NaN   C85        S
freq            NaN        NaN        NaN      1     5        NaN        NaN        NaN          1        NaN     1        7
mean        5.50000   0.500000   2.300000    NaN   NaN  27.250000   0.700000   0.300000        NaN  27.844990   NaN      NaN
std         3.02765   0.527046   0.948683    NaN   NaN  15.736672   0.948683   0.674949        NaN  23.018405   NaN      NaN
min         1.00000   0.000000   1.000000    NaN   NaN   2.000000   0.000000   0.000000        NaN   7.250000   NaN      NaN
25%         3.25000   0.000000   1.250000    NaN   NaN  20.000000   0.000000   0.000000        NaN   8.820825   NaN      NaN
50%         5.50000   0.500000   3.000000    NaN   NaN  26.500000   0.500000   0.000000        NaN  18.887500   NaN      NaN
75%         7.75000   1.000000   3.000000    NaN   NaN  35.750000   1.000000   0.000000        NaN  46.414575   NaN      NaN
max        10.00000   1.000000   3.000000    NaN   NaN  54.000000   3.000000   2.000000        NaN  71.283300   NaN      NaN

Missing Values:
 PassengerId    0
Survived       0
Pclass         0
Name           0
Sex            0
Age            2
SibSp          0
Parch          0
Ticket         0
Fare           0
Cabin          6
Embarked       0
dtype: int64
d:\karthikeyan_elivatelab\task2.py:22: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  df['Age'].fillna(df['Age'].median(), inplace=True)
d:\karthikeyan_elivatelab\task2.py:23: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.


  df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
