# 30 - File IO
## Reading Files
- You can read a file with `open` function
- `open` returns a file object
- You can read a file object with the read method

```python
file = open('story.txt')
file.read()
```

## Cursor Movement
- Python reads files by using a cursor
- This is like the cursor you see when you are typing
- After a file read, the cursor is at the end
- To move the cursor, use the `seek` method

## Closing a File
- You can close a file with the close method
- You can check if a file is closed with the closed attribute
- Once closed, a file can't be read again
- Always close files, it frees up system resources

## with Blocks
- It gives us cleaner syntax
- It doesn't need to add `close`
```python
with open('file.txt') as f:
  f.read()
```

## Writing to Text Files
- You can also use `open` to `write` to a file
- Need to specify the "w" flag as the second argument

## Modes for Opening Files
- r -  Read a file
- w - Write to a file
- a - Append to a file
- r+ - Read and write to a file
