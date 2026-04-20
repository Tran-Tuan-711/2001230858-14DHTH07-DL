import pandas as pd

# Series Object

a = pd.Series([1., 2., 3.])
print(a)
print('First value: ', a[0]) # Lấy giá trị đầu tiên

b = pd.Series([1., 2., 3.], index=['x', 'y', 'z'])
print(b)
print('First value: ', b['x']) # Lấy giá trị đầu tiên theo index

# Tao pandas series tu dictionary
calories = {'day1': 420, 'day2': 380, 'day3': 390}
myvar = pd.Series(calories)
print(myvar)