# 29 - Testing with Python

## Why test?
- Reduce bugs in existing code
- Ensure bugs that are fixed stay fixed
- Ensure that new features don't break old ones
- Ensure that cleaning up code doesn't introduce new bugs

## Test Driven Development
- Development begins by writing tests
- Once tests are written, write code to make tests pass
- Once tests pass, a feature is considered complete

### Red, Green, Refactor
1. Red - Write s test that fails
2. Green - Write the minimal amount of code necessary to make the test pass
3. Refactor - Clean up the code, while ensuring that tests still pass

## Assertions
- We can make simple assertions with the `assert` keyword
- `assert` accepts an expression
- Returns `None` if the expression is truthy
- Raises an `AssertionError` if the expression is falsy
- Accepts an optional error message as a second argument

```python
def add_positive_numbers(x, y):
    assert x > 0 and y > 0, 'Both numbers must be positive'
    return x + y

add_positive_numbers(1, 1)  ## 2
add_positive_numbers(1, -2) ## AssertionError: Both numbers must be positive
```

### Assertions Warning
If a Python file run with the -O flag, assertions will not be evaluated

## doctests
- We can write tests for functions inside of the docstring
- Write code that looks like it is inside of a REPL

```python
def add(x, y):
    '''add together x and y

    >>> add(1, 2)
    3

    >>> add(8, 'hi')
    TracebackError (most recent call last):

    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    '''
```
### Issues with doctests
- Syntax is a little strange
- Clutters up our function code
- Lacks many features of largers testing tools
- Tests can be brittle

## Unit Testing
- Test smallest parts of an application in isolation (e.g. units)
- Good candidates for unit testing: individual classes, modules, or functions
- Bad candidates for unit testing: an entire application, dependencies across several classes or modules

### unitests
- Python comes with a built-in module called `unittest`
- You can write unit tests encapsulated as classes that inherit from `unittest.TestCase`
- This inheritance gives you access to many assertion helpers that let you test the behavior of your functions

`test.py`
```python
import unittest
from activities import eat, nap

class ActivityTests (unittest.TestCase):
    def test_eat(self):
        self.assertionEqual(eat('brocoli', is_healthy=True), 'I´m eating brocoli, because my body is a temple')
        self.assertionEqual(eat('pizaa', is_healthy=False), 'I´m eating brocoli, because YOLO')

if __name__ == '__main__':
    unittest.main()
```
This code will test the function eat from activities.py

`activities.py`
```python
def eat(food, is_healthy):
    ending = 'because YOLO'
    if is_healthy:
        ending = 'because my body is a temple'
    return f'I´m eating {food}, {ending}'
```

## Types of Assertions
- `self.assertEqual()`
- `self.assertNotEqual()`
- `self.assertTrue()`
- `self.assertFalse()`
- `self.assertIsNone()`
- `self.assertIsNotNone()`
- `self.assertIn()`
- `self.assertNotIn()`

## setUp and tearDown
- For larger applications, you may want similar application state before running tests.
- setUp runs before each test method
- tearDown runs after each test method
- Common use cases: adding/removing data from a test database, creating instances of a class
