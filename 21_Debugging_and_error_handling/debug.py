def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    if type(text) is not str:
        raise TypeError('Text must be str')    
    if color not in colors:
        raise ValueError('Color is invalid color')

    print(f'Printed {text} in {color}')

colorize('hola', 'cyan')
#colorize(1,'red')