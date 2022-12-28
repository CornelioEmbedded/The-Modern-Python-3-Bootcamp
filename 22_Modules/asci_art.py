import pyfiglet
import termcolor

msg = input('Type something: ')
color_chose = input('Type a color: ')

ascii = pyfiglet.figlet_format(msg)
final_text = termcolor.colored(ascii, color=color_chose)
print(final_text)