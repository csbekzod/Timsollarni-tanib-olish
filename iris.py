# ROE001-L2, Abduxalilov Bekzod 1-amaliy
import pandas 

data = pandas.read_csv('iris_ml.csv')
# print(data.head()) head() funksiyasi default xolatda 5qator malumotni chiqarib beradi.
data = data[['sepallength','sepalwidth','petallength','petalwidth']]
data = data.values.tolist()
print(data)

g = int(input('g koefitsiyentni kiriting: '))
iris_array = []

for i in range(1, 5):
    attr_value = round(float(input(f'irisning {i} - atributini qiymatini kiriting:')))
    iris_array.append(attr_value)

print(iris_array)

result_array = []
for i in range(len(data)):
    count = 0
    for j in range(len(data[i])):
        if round(data[i][j]) == iris_array[j]:
            count += 1
    result_array.append(count)
print(result_array)

helper_array = []


def func(g):
      for x in result_array:
          helper_array.append(1) if x>=g else helper_array.append(0)

func(g)
print('helper_array', helper_array)

class1, class2, class3 = sum(helper_array[:50]) , sum(helper_array[50:100]), sum(helper_array[100:])

if class1 > class2 and class1 > class3:
    print('class 1 ga ovoz')
    
elif class2 > class1 and class2 > class3:
    print('class 2 ga ovoz')
    
elif class3 > class1 and class3 > class2:
    print('class 3 ga ovoz')
    
else:
    print('class mavjud emas!')
    
print('class 1 ga ovoz:', class1)
print('class 2 ga ovoz:', class2)
print('class 3 ga ovoz:', class3)
