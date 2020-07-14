import numpy as np
from tabulate import tabulate
# from tabulte import 


sl_no = np.arange(1,16)
Mahabharatha_Charactor = ['arjunan','bhema','bhisma','yudhestra','nagula','sahadeva','karna',
        'duriyodhana','duchathana','krishna','drona','ashwatama','kripa','vidhura',
        'godothgaja',]

Age_of_death = [75,77,768,79,73,71,86,79,78,81,74,167,180,45]

Ayudha = ['kaandipam','gadha','dhanush','spear','vaal','vaal','vijaya',
          'gadha','gadha','chakra','dhanush','dhanush','dhanush','dhanush',
          'gadha']

table = zip(sl_no,Mahabharatha_Charactor,Age_of_death,Ayudha)
headers = ['sl_no','Mahabharatha_Charactor','Age_of_death','Ayudha']

# print(tabulate(table, headers, tablefmt="rst"))
# print(tabulate(table, headers, tablefmt="psql"))
print(tabulate(table, headers, tablefmt="pretty"))
# print(tabulate(table, headers, tablefmt="presto"))
# print(tabulate(table, headers, tablefmt="orgtbl"))
# print(tabulate(table, headers, tablefmt="pipe"))
# print(tabulate(table, headers, tablefmt="fancy_grid"))
# print(tabulate(table, headers, tablefmt="grid"))


aa = tabulate(table, headers, tablefmt="pretty")

np.save('geetha',aa)

