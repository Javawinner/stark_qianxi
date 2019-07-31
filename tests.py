# class Student(object):
#
#     @property
#     def get_score(self):
#         return self._score
#
#     @get_score.setter
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
#
# s = Student()
# # s.set_score(60)
# # print(s.get_score())
#
# s.set_score = 60
# print(s.get_score)

class A:
    def __init__(self):
        self.__name = 'lxx'

    @property  # 将方法装饰成类的属性
    def xxx(self):
        return self.__name

    @xxx.setter  # 给装饰成类的属性的方法赋值
    def xxx(self, v):
        self.__name = v

# 获取初始值
a = A()
print(a.xxx)

# 设置值
a.xxx = 'lyy'
print(a.xxx)
print(a.xxx)