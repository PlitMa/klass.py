grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#это функция позволяет сделать сортировку по алфавитному порядку по умолчанию#
students = sorted(students)
 #Высчитываем среднее арифметическое кажого ученика. Sum -  это сложение всех чилел, len - это колличество объектов#
a = sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])
 #Чтобы сделать словарь учеников и с их оценками следует прописать ключ и его значение#
klass = {students[0]: a[0], students[1]: a[1], students[2]: a[2], students[3]: a[3], students[4]: a[4]}
print(klass)