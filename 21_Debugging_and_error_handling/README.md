# 21 - Debugging and error handling

## Types of errors

We need to understand common Python errors

**SyntaxError**: Occurs when Python encounters incorrect syntax.

**NameError**: Occurs when a variable is not defined.

**TypeError**: Occurs when an operation or funtion is applied to the wrong type or Python cannot interpret an operation on two data types.

**IndexError**: Occurs when you try to access an element in a list using an invalid index.

**ValueError**: Occurs when a built-in operation or function receives an argument that has the right type but an inappropiate value

**KeyError**: Occurs when a dictionary doesn´t have a specific key.

**AttributeError**: Occurs when a variable doesn´t have an attribute.

## Raise errors

We can raise errors in Python code

Example of raise TypeError for known if the text parameter is a str or not.

```python

def colorize(text, color):
    if type(text) is not str:
        raise TypeError('Text must be str')    
    print(f'Printed {text} in {color}')

colorize('hola', 'red')
colorize(1,'red')

```

## Handle Errors

In Python is strongly encouraged to use try/except blocks to catch exceptions when we can do something about them.

```python
try:
    whatever
except:
    print('PROBLEM'!)
```

We can handle errors with try - except syntax, but we can use else and finally too.

```python
try:
    num = int(input('Type a number: '))
except ValueError:
    print('That´s not a number')
else:
    print('I don´t care if it´s a number')
finally:
    print('I will show no matter what')
```

else executes in the code if except is not handling.

finaly executes in the code no matter what.