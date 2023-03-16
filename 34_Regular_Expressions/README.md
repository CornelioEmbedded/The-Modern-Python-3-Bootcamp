# 34- Regular Expressions

## Potential Use Cases
- Credit Card number validating
- Phone number validating
- Advanced find/replace in text
- Formatting text/output
- Syntax highlighting

## Some Regex Syntax
- `\d`: digit 0-9
- `\w`: letter, digit, or underscore
- `\s`: whitespace character
- `\D`: not a digit
- `\W`: not a word character
- `\S`: not a whitespace character
- `.`: any character except line break
- `+`: One or more
- `{3}`: Exactly x times. {3} - 3 times
- `{3, 5}`: Three to five times
- `{4,}`: Four or more times
- `*`: Zero or more times
- `?`: Once or none (optional)

## Anchors and Boundaries
- `^`: Start of string or line
- `$`: End of string or line
- `\b`: Word boundary

## Regular Expressions in Python

```python
import re
pattern = re.compile(r'\d{3}-\d{4}')
match = pattern.search(123-1234)
print(match.group)
```

```python
import re

def extract_phone(input):
  phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
  match = phone_regex.search(input)
  if match:
    return match.group()
  return None
 ```
 
