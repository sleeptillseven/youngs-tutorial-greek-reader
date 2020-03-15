import re
from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('index.html.jinja')

f = open('text/tutorial-greek-reader.txt', 'r')
text = f.readlines()
f.close()

output = template.render(rows=text)
print(output)
