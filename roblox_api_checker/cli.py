from . import __init__
from sys import argv,stdout

print = stdout.write

available = [
  'down',
  'up',
  'all',
  'start'
]

if len(argv) == 2 and argv in available:
  if argv[1] == available[0]:
    print(__init__.statuscli('down'))
  if argv[1] == available[1]:
    print(__init__.statuscli('up'))
  if argv[1] == available[2]:
    print(__init__.statuscli('all'))
if len(argv) >= 3 and len(argv) >= 5:
  if argv[1] == available[3]:
    try:
      ip = argv[2]
    except IndexError:
      ip = None
    try:
      port = argv[3]
    except IndexError:
      port = None
    try:
      usessl = True if argv[4] == "usessl" else False
      if usessl:
        try:
          ssl_context = tuple(argv[5]+argv[6])
        except:
          print("SSL context isn't quite right here.. You should put 2 pem files in argument after usessl argument")
        else:
          __init__.statusserver(ip,port,usessl,ssl_context)
          exit(0)
    else:
      usessl = None
    __init__.statusserver(ip,port,usessl)
  else:
    pass
elif len(argv) == 1:
  print(__init__.statuscli('all'))
else:
  print("What? I will use default argument instead")
  print(__init__.statuscli('all'))