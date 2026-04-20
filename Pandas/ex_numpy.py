import numpy as np


# Array 1 Chiều
my_list = [1,9,15,39]
print('Python list', my_list)
#  C1
my_numpy_array = np.array(my_list)
print('Numpy array:', my_numpy_array)
# C2
a = np.array([1,9,15,39])
print(a)


print('='*30)
# Array 2 Chiều
c = np.array([(1,2,3),(4,5,6)])

print(c)
print(c.shape) # Kích thước của mảngpython ex_numpy.py
print(c.dtype) # Kiểu dữ liệu của mảng  

print('='*30)
# Reshape mảng thay dổi kích thước của mảng
e = np.array([[1.,2.,3.],[4.,5.,6.]])
print(e)
print('mang ban dau\n', e.shape)

f = e.reshape(3,2)
print('mang sau khi reshape\n', f)

print('='*30)
# platten chuyen doi mang 2 chieu thanh mang 1 chieu

f = e.flatten()
print('mang sau khi flatten\n', f)


print('='*30)
# hstack((x,y)) Nối hai mảng theo chiều ngang
# vstack((x,y)) Nối hai mảng theo chiều dọc

hsArray1 = np.array([1.,2.,3.])
hsArray2 = np.array([4.,5.,6.])
print('Nối hai mảng theo chiều ngang\n', np.hstack((hsArray1, hsArray2)))
print('Nối hai mảng theo chiều dọc\n', np.vstack((hsArray1, hsArray2)))

print('='*30)
# Sinh mang so nguyen ngau nhien

randomIntArray = np.random.randint(100, size=(5,))
print('Mang so nguyen ngau nhien\n', randomIntArray)
randomIntArray2 = np.random.randint(100, size=(3,4))
print('Mang so nguyen ngau nhien 2 chieu\n', randomIntArray2)

print('='*30)
# Sinh mang ngau nhien theo chuan Gaussian
# Numpy.random.normal(loc=0.0, scale=1.0, size=None)
# loc: trung bình của phân phối
# scale: độ lệch chuẩn của phân phối
# size: kích thước của mảng kết quả

randomNormalArray = np.random.normal(5, 0.5, 10)
print('Mang ngau nhien theo chuan Gaussian\n', randomNormalArray)

print('='*30)
# Sinh mang ngau nhien tu mot gia tri cho truoc

randomFromValueArray = np.random.choice([10,20,30,40])
print('Gia tri ngau nhien tu mot mang cho truoc\n', randomFromValueArray)

randomFromValueArray2 = np.random.choice([10,20,30,40], size=(3,4))
print('Mang ngau nhien tu mot mang cho truoc\n', randomFromValueArray2)

print('='*30)
# Thay doi gia tri cua ma tran
matrix = np.matrix(np.ones((5,5)))
print('Ma tran ban dau\n', matrix)

np.array(matrix)[2] = 5
print('Ma tran sau khi thay doi voi array\n', matrix)

np.asarray(matrix)[2] = 2
print('Ma tran sau khi thay doi voi asarray\n', matrix)

print('='*30)
# Sinh day so theo khoang cho truoc
# Ham arange

a = np.arange(1, 20)
print('Day so tu 1 den 20\n', a)

b = np.arange(1, 20, 2) # Day so tu 1 den 20 voi buoc nhay la 2
print('Day so tu 1 den 20 voi buoc nhay la 2\n', b)

# Ham linspace
c = np.linspace(1, 20, 10) # Day so tu 1 den 20 voi 10 phan tu
print('Day so tu 1 den 20 voi 10 phan tu\n', c)

print('='*30)
# Slice
a = np.array([(1, 2, 3), (4, 5, 6)])
print('Mang ban dau\n', a)
print('First row:', a[0]) # Lấy hàng đầu tiên
print('Second row:', a[1]) # Lấy hàng thứ hai

# Indexing
print('First column:', a[:, 0]) # Lấy cột đầu tiên
print('Second column:', a[:, 1]) # Lấy cột thứ hai
print('First two values of second row:', a[1, :2]) # Lấy hai giá trị đầu tiên của hàng thứ hai
