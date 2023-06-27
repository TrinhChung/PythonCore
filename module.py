def helloWord():
    print("Hello World3!")

class Animal:
    "Class for Animal"

    name = "Animal"
    __type_Animal = 0
    
    def __init__(self, name,type):
        self.name = name
        self.__type_Animal = type

    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.__type_Animal
    
    def setValueType(self,value):
        print(value);

class Dog(Animal):
    line = "Ngao";
    def __init__(self, name, type ,line):
        super().__init__(name,type)
        self.line = line
    
    def get_line(self):
        return self.line
    
    @classmethod
    def create_dog_by_name(cls, name):
        return cls(name, 2, name + "Dog")

    @staticmethod
    def isDog(type):
        return type == 2;

from functools import wraps

def new_decorator (func):
    @wraps (func) # "Tránh ghi đè tên wrap bọc thay vì tên hàm muốn bọc"
    def wrap_the_func ():
        print("I am doing some boring work before executing func()" )
        func()
        print("I am doing some boring work after executing func()" )
    return wrap_the_func

@new_decorator
def func_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to ""remove my foul smell")

