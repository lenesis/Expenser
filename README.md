# Expenser

Save a list of the things you have spent money for in a sql database and access it whenever you want!

## usage


### init
To initialise program database for the first time run the following command:
'''bash
python expenser.py --init
'''

### add
To add new items to the database:
'''bash
python expenser.py --add <amount> <category> [<messege>]
'''
- amount: the amount of money 
- category: the category of what you have spent money for
- messege: any comments about your new item (optional)

### show
To see your saved items:
'''bash
python expenser.py --show [<category>]
'''
this will show all items/selected category items.