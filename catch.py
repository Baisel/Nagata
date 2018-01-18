import cgi
from controllers.controller import defaultPosition, dragMove


with open('flag.txt', 'r') as f:
    flag = f.readline()
    if flag == 'start':
        form = cgi.FieldStorage()
        count = int(form['count'].value)
        defaultPosition()
        dragMove(count)

