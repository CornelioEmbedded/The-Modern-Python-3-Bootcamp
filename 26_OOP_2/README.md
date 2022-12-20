# 24 - Object Oriented Programming 2

## Inheritance
A key feature of OOP is the ability to define a class which inherits from another class (a "base" or "parent" class).

In Python, inheritance works by passing the parent class as an argument to the definition of a child class:

```python
class Animal:
    cool = True

    def make_sound(self, sound):
        print(f'This animal says {sound}')

class Cat(Animal):
    pass
```
## @property
We can convert methods into variables using @property, as I understood

```python
@property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError('age cant be negative')
```

## super()
It allows us to not repeting variables or attributes in a class, if a class inherits from another class.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f'This animal says {sound}')

    def __repr__(self):
        return f'{self.name} is a {self.species}'

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species='Cat')
        self.breed = breed
        self.toy = toy
    
    def play(self):
        print(f'{self.name} plays with {self.toy}')
```

## Multiple inheritance
We can have multiple inheritane, where more than one function is "like a father" from another function, and that function recieves both functionality like methods.

```python
class Aquatic:
    def __init__(self, name):
        self.name = name
    
    def swim(self):
        return f'{self.name} is swimming'
    
    def greet(self):
        return f'I am {self.name} of the sea!'

class Ambulatory:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        return f'{self.name} is walking'
    
    def greet(self):
        return f'I am {self.name} of the land'

class Penguin(Aquatic, Ambulatory):
    def __init(self, name):
        super().__init__(name=name)
```

## Method Resolution Order (MRO)

Whenever you create a class, Python sets a Method Resolution Order, or MRO, for that class, which is the order in which Python willlook for methods on instances of that class.

You can programmatically reference the MRO three ways:
- `__mro__` attribute on the class
- use the mro() method on the class
- use the builtin help(cls) method

## Polymorphism
An object can take on many forms.
- The same class method works in a similar way for different classes.
- The same operation works for different kinds of objects.


## Special `__magic__` methods
If we want to add more functions into classes, we can use magic methods. It let us to use len(Class), add and substract in classes.

```python
def __repr__(self):
    return 'Hi, I`m a magic method '
```

