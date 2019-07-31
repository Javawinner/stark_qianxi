class Foo(object):
    pass


# 实例化了一个Foo类的对象
obj1 = Foo()

print(obj1)  # <__main__.Foo object at 0x10846e240>

# 再次实例了一个对象
obj2 = Foo()
print(obj2)  # <__main__.Foo object at 0x10846e278>
