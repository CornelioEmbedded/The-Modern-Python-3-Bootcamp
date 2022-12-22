# 28 - Decorators
- Decprators are functions
- Decorators wrap other functions and enhance their behavoir
- Decorators are examples of higher order functions
- Decorators have their own syntax, using "@" (syntantic sugar)

```python
def be_polite(fn):
  def wrapper():
    print('What a pleasure to meet you!')
    fn()
    print('Have a great day')
  return wrapper

@be_polite
def greet():
  print('My name is Cornelio')
```
