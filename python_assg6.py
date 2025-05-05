# 1. Using self
print("1. Using self")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Ali", 90)
s1.display()

# 2. Using cls
print("\n2. Using cls")
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

c1 = Counter()
c2 = Counter()
Counter.show_count()

# 3. Public Variables and Methods
print("\n3. Public Variables and Methods")
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting.")

car = Car("Toyota")
print(car.brand)
car.start()

# 4. Class Variables and Class Methods
print("\n4. Class Variables and Class Methods")
class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
print(b1.bank_name)
Bank.change_bank_name("XYZ Bank")
print(b1.bank_name)
print(b2.bank_name)

# 5. Static Variables and Static Methods
print("\n5. Static Variables and Static Methods")
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 7))

# 6. Constructors and Destructors
print("\n6. Constructors and Destructors")
class Logger:
    def __init__(self):
        print("Logger initialized.")

    def __del__(self):
        print("Logger destroyed.")

logger = Logger()
del logger

# 7. Access Modifiers: Public, Private, Protected
print("\n7. Access Modifiers: Public, Private, Protected")
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("John", 50000, "123-45-6789")
print(emp.name)
print(emp._salary)
try:
    print(emp.__ssn)
except AttributeError:
    print("Cannot access private variable __ssn")

# 8. The super() Function
print("\n8. The super() Function")
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Sara", "Math")
print(f"Name: {t.name}, Subject: {t.subject}")

# 9. Abstract Classes and Methods
print("\n9. Abstract Classes and Methods")
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(4, 5)
print(rect.area())

# 10. Instance Methods
print("\n10. Instance Methods")
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

d = Dog("Buddy", "Golden Retriever")
d.bark()

# 11. Class Methods
print("\n11. Class Methods")
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)

# 12. Static Methods
print("\n12. Static Methods")
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(30))

# 13. Composition
print("\n13. Composition")
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

engine = Engine()
car = Car(engine)
car.start_engine()

# 14. Aggregation
print("\n14. Aggregation")
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

emp = Employee("Ayesha")
dept = Department(emp)
print(dept.employee.name)

# 15. Method Resolution Order (MRO) and Diamond Inheritance
print("\n15. MRO and Diamond Inheritance")
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()

# 16. Function Decorators
print("\n16. Function Decorators")
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()

# 17. Class Decorators
print("\n17. Class Decorators")
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.greet())

# 18. Property Decorators
print("\n18. Property Decorators")
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

prod = Product(100)
print(prod.price)
prod.price = 150
print(prod.price)
del prod.price

# 19. callable() and __call__()
print("\n19. callable() and __call__()")
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

m = Multiplier(3)
print(callable(m))
print(m(5))

# 20. Creating a Custom Exception
print("\n20. Creating a Custom Exception")
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)

# 21. Make a Custom Class Iterable
print("\n21. Custom Class Iterable")
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

for number in Countdown(5):
    print(number)
