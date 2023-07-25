#Lenesis
import api
from tabulate import tabulate
from docopt import docopt

usage= '''*********Expenser********

Usage:
expenser-cli.py --init
expenser-cli.py --show [<category>]
expenser-cli.py --add <amount> <category> [<messege>]
expenser-cli.py --help'''

cmd = docopt(usage)

if cmd['--init']:
    api.init()
    print ('table created!')
if cmd['--show']:
    cat = cmd['<category>']
    if cat:
        data = api.showSpent(cat)
        print (f'total expense: {data[0]}')
        print (tabulate(data[1]))
    else:
        data = api.showSpent()
        print (f'total expense: {data[0]}')
        print (tabulate(data[1]))
if cmd['--add']:
    if cmd['<amount>'] and cmd['<category>']:
        if cmd['<messege>']:
            api.addSpent(cmd['<amount>'], cmd['<category>'], cmd['<messege>'])
        else:
            api.addSpent(cmd['<amount>'], cmd['<category>'])
    


