import numpy as np
import pandas as pd

# Bai 1
print('='*30, 'Bai 1', '='*30)
arr = np.random.randint(0, 21, (3, 3))
print(arr)

print(np.all(arr != 0))

# Bai 2
print('='*30, 'Bai 2', '='*30)
arr = np.random.randint(0, 21, (3, 3))
print(arr)

print(np.any(arr != 0))

# Bai 3
print('='*30, 'Bai 3', '='*30)
a = np.array([1, 2, 3])
b = np.array([2, 2, 1])

print(np.greater(a, b))
print(np.greater_equal(a, b))
print(np.less(a, b))
print(np.less_equal(a, b))

# Bai 4
print('='*30, 'Bai 4', '='*30)
arr = np.arange(1, 11)
print(arr[arr > 5])

# Bai 5
print('='*30, 'Bai 5', '='*30)
arr = np.random.randint(30, 71, 50)
print(arr)

# Bai 6
print('='*30, 'Bai 6', '='*30)
print(np.identity(3))\

# Bai 7
print('='*30, 'Bai 7', '='*30)
arr = np.random.randint(15, 56, 10)
print(arr)

arr[1:] = 0
print(arr)

# Bai 8
print('='*30, 'Bai 8', '='*30)
arr = np.random.randint(0, 21, 20)
print(arr)

arr[(arr >= 9) & (arr <= 15)] *= -1
print(arr)

# Bai 9
print('='*30, 'Bai 9', '='*30)
arr = np.random.randint(10, 22, (3, 4))
print(arr)

# Bai 10
print('='*30, 'Bai 10', '='*30)
arr = np.ones((10, 10))
arr[1:-1, 1:-1] = 0
print(arr)

# Bai 11
print('='*30, 'Bai 11', '='*30)
arr = np.diag([1, 2, 3, 4, 5])
print(arr)

# Bai 12
print('='*30, 'Bai 12', '='*30)
arr = np.random.randint(0, 10, (3, 3, 3))
print(arr)

print("Sum theo dòng:", arr.sum(axis=1))
print("Sum theo cột:", arr.sum(axis=2))

# Bai 13
print('='*30, 'Bai 13', '='*30)
a = np.random.randint(0, 10, 10)
b = np.random.randint(0, 10, 10)

print(np.dot(a, b))

# Bai 14
print('='*30, 'Bai 14', '='*30)
A = np.random.randint(0, 10, (4, 3))
y = np.random.randint(0, 10, 3)

print(A)
print(y)

result = A + y
print(result)

# Bai 15
print('='*30, 'Bai 15', '='*30)
s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 10])

print(s1 + s2)
print(s1 - s2)
print(s1 * s2)
print(s1 / s2)

# Bai 16
print('='*30, 'Bai 16', '='*30)
df = pd.DataFrame({
    'col1': [1,2,3,4,7,11],
    'col2': [4,5,6,9,5,0],
    'col3': [7,5,8,12,1,11]
})

print(df['col1'])

# Bai 17
print('='*30, 'Bai 17', '='*30)
df = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=['A','B','C'])
print(df.sort_index(axis=1))

# Bai 18
print('='*30, 'Bai 18', '='*30)
s = pd.Series([1,2,3,4,5], index=['A','B','C','D','E'])
print(s.reindex(['B','A','C','D','E']))

# Bai 19
print('='*30, 'Bai 19', '='*30)
sr1 = pd.Series([1,2,3,4,5])
sr2 = pd.Series([2,4,6,8,10])

print(sr1[~sr1.isin(sr2)])

# Bai 20
print('='*30, 'Bai 20', '='*30)
a = np.random.randint(0, 20, 20)
b = np.random.randint(0, 20, 20)

print(np.union1d(a, b))
print(np.intersect1d(a, b))

# Bai 21
print('='*30, 'Bai 21', '='*30)
x = pd.Series(range(10))
y = pd.Series(list("pqrstuvwxy"))

# vertical
print(pd.concat([x, y]))

# horizontal
print(pd.concat([x, y], axis=1))


exam_data = {
'name': ['Anastasia','Dima','Katherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
'score': [12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
'attempts': [1,3,2,3,2,3,1,1,2,1],
'qualify': ['yes','no','yes','no','no','yes','yes','no','no','yes']
}
labels = list('abcdefghij')

df = pd.DataFrame(exam_data, index=labels)

# Bai 22
print('='*30, 'Bai 22', '='*30)
print(df)

# Bai 23
print('='*30, 'Bai 23', '='*30)
print(df.head(3))

# Bai 24
print('='*30, 'Bai 24', '='*30)
print(df[['name','score']])

# Bai 25
print('='*30, 'Bai 25', '='*30)
print(df[df['attempts'] > 2])

# Bai 26
print('='*30, 'Bai 26', '='*30)
print(df.shape)

# Bai 27
print('='*30, 'Bai 27', '='*30)
print(df[df['score'].isnull()])

# Bai 28
print('='*30, 'Bai 28', '='*30)
print(df[df['score'].between(15,20)])

# Bai 29
print('='*30, 'Bai 29', '='*30)
print(df[(df['attempts'] > 2) & (df['score'].between(15,20))])

# Bai 30
print('='*30, 'Bai 30', '='*30)
df.loc['d','score'] = 19
print(df)