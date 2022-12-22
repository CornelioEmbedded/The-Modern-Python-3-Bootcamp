# 27 - Iterators and Generators

## Iterators and Interables
- Interator: An object that can be iterated upon. An object which returns data, one element at a time when next() is called on it.
- Iterable: An object which will return an Iterator when iter() is called on it.

```python
def my_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      thing = next(iterator)
    except StopIteration:
      break
 ```
 
 ## Generators
 - Generators are iterators
 - Generators can be created with generator functions
 - Generators functions use the yield keyword
 - Generators can be created with generator expressions
 
 
