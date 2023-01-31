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