# 24 - Object Oriented Programming

## What is OOP?
Object Orented Programming is a method of programming that attempts to model some process or thing in the world as a class or object.

- Class: A blueprint for objects. Classes can contain methods (functions) and attributes (similar to keys in a dict)
- Instance: Objects that are constructed from a class blueprint that contain ther class´s methods and properties.

## Why OOP?
With object oriented programming, the goal is to encapsulate your code into logical, hierarchical groupings using classes so that you can reason about your code at a higher level.

## Encapsulation
The grouping of public and private attributes and methods into programmatic class, making abstraction possible.

## Abstraction
Exposing only relevant data in a class interface, hiding private attirbutes and methods form users.

## Creating a Class
Classes in Python can have a special `__init__` method, which gets called every time you create an instance of the class. Here we initialize data.

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
```

## Instantiating a Class
Creating an object is an instance of a class is called instantiating a class

```python
v = Vehicle('Kia', 'Rio', 2022)
```

## self
The self keyword refers to the current class instance. Self must always be the first parameter to `__init__` and any methods and properties on class instances.

```python
class User:
    def __init__(self, first, last, age):
        self.name = first
        self.last = last
        self.age = age
```

## Instance Attributes and Methods

```python
class User:
    def __init__(self, first, last, age):
        self.name = first
        self.last = last
        self.age = age
    
    def full_name(self):
        return f'{self.name} {self.last}'
    
    def initials(self):
        return f'{self.name[0]}.{self.last[0]}.'
    
    def likes(self, thing):
        return f'{self.name} likes {thing}'
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age+=1
        return f'Happy {self.age}th, {self.name}'
```

## Class Attributes
We can also define attributes directly on a class that are shared by all instances of a class and the class itself.

```python
class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']  ## Class attribute
    def __init__(self, name, species):
        if species not in self.allowed:
            raise ValueError(f'You can have a {species} as a pet!')
        self.name = name
        self.species = species
    
    def set_species(self, species):
        if species not in self.allowed:
            raise ValueError(f'You can have a {species} as a pet!')
        self.species = species
```

## Class Methods
Class methods are methods (with the @classmethod decorator) that are not concerned with instances, but the class itself.

```python
    @classmethod
    def display_active_users(cls):
        return f'There are {cls.active_users} active users'
    
    @classmethod
    def from_string(cls, data):
        first, last, age = data.split(',')
        return cls(first, last, int(age))
```

## String Representation Example
The '__repr__' method is one of several ways to provide a nicer string representation.