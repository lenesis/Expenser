#Lenesis
import api
import os, sys
#Check if required modules are installed
try:
    from tabulate import tabulate
    from docopt import docopt
    import termcolor
except ImportError:
    if sys.platform.startswith('linux'):
        os.system('pip3 install tabulate docopt termcolor')
    elif sys.platform.startswith('freebsd'):
        os.system('pip3 install tabulate docopt termcolor')
    else:
        os.system('pip install tabulate docopt termcolor')

termcolor.cprint('''
_______ ___   ___ .______    _______ .__   __.      _______. _______ .______      
|   ____|\  \ /  / |   _  \  |   ____||  \ |  |     /       ||   ____||   _  \     
|  |__    \  V  /  |  |_)  | |  |__   |   \|  |    |   (----`|  |__   |  |_)  |    
|   __|    >   <   |   ___/  |   __|  |  . `  |     \   \    |   __|  |      /     
|  |____  /  .  \  |  |      |  |____ |  |\   | .----)   |   |  |____ |  |\  \----.
|_______|/__/ \__\ | _|      |_______||__| \__| |_______/    |_______|| _| `._____|

𝐷𝑜𝑛'𝑡 𝑚𝑖𝑠𝑠 𝑎𝑛𝑦 𝑚𝑜𝑛𝑒𝑦 𝑦𝑜𝑢 ℎ𝑎𝑣𝑒 𝑠𝑝𝑒𝑛𝑡
                                                                                                    
      ''', 'green')
        

usage= '''*********Expenser********

Usage:
expenser.py --init
expenser.py --show [<category>]
expenser.py --add <amount> <category> [<messege>]
expenser.py --help'''

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
    


