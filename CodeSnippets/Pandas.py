# Pandas DataFrames
# Pandas is a high-level data manipulation tool developed by Wes McKinney. It is built on the Numpy 
# package and its key data structure is called the DataFrame. DataFrames allow you to store and 
# manipulate tabular data in rows of observations and columns of variables.

# There are several ways to create a DataFrame. One way way is to use a dictionary. For example:

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"], "capital": ["Brasilia","Moscow", "New Dehli", "Beijing", "Pretoria"], "area": [8.516, 17.10, 3.286, 9.597, 1.221], "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# As you can see with the new brics DataFrame, Pandas has assigned a key for each country as the 
# numerical values 0 through 4. If you would like to have different index values, say, the two 
# letter country code, you can do that easily as well.

# Set the index for brics
brics.indes = ["BR", "RU", "IN", "CH", "SA"]

# print out brics with new index value
print(brics)

# 
# Another way to create a DataFrame is by importing a csv file using Pandas. Now, the csv cars.csv 
# is stored and can be imported using pd.read_csv:

# import pandas as pd
import pandas as pd

# import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# print out cares
print(cars)

# Indexing DataFrames
# There are several ways to index a Pandas DataFrame. One of the easiest ways to do this is by using 
# square bracket notation.

# In the example below, you can use square brackets to select one column of the cars DataFrame. 
# You can either use a single bracket or a double bracket. The single bracket will output a Pandas 
# Series, while a double bracket will output a Pandas DataFrame.

# import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# print out country column as Pandas Series
print(cars['cars_per_cap'])

# print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# Square brackets can also be used to access observations (rows) from a DataFrame. For example:

# import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# print out first 4 observations (rows)
print(cars[0:4])

# print out fifth and sixth observation (rows)
print(cars[4:6])

# You can also use loc and iloc to perform just about any data selection operation. loc is label-based, 
# which means that you have to specify rows and columns based on their row and column labels. iloc 
# is integer index based, so you have to specify rows and columns by their integer index like you did 
# in the previous exercise.

# import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# print out observation for Japan
print(cars.iloc[2])

# print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

