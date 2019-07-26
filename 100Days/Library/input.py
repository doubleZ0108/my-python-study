# input -> 将输入的信息直接进行分割 并 创建对象

class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return '这是%d岁的%s' % (self._age,self._name)

def input_Student():
    # 将输入的信息分割
    name_str, age_str = input('请输入学生 姓名 年龄(以空格隔开)').split(' ')
    return name_str,int(age_str)

if __name__ == "__main__":
    total_stu = 3
    students = []
    for _ in range(total_stu):
        students.append(Student(*input_Student()))  # 注意这里有个🌟

    for student in students:
        print(student)
