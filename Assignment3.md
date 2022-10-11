Problem 1: Wallets

Write a Python program that request a user to provide numbers representing the value in cash for different wallets. Your program should store these values in a list. The user should be able to add as many values as they want. One example of a filled `wallets` list (in this example, with 5 wallets) would be:

```
print(wallets)

Output: [1023, 984, 192, 1842, 12]
```

After the user adds the values for the wallets, your application should provide the following information:
* The fattest wallet has `$value` in it.
* The skinniest wallet has `$value` in it.
* All together, these wallets have `$value` in them.
* All together, the total value of these wallets is worth `$value` dimes.

Please try to think about different functions to complete your work.

Problem 2: Periodic Table 

The Periodic Table of the Elements was developed to organize information about the elements that make up the Universe.
Write a terminal application that lets you enter information about each element in the periodic table.
Make sure you include the following information:
* symbol, name, atomic number, row, and column

You must save the elements in a dictionary where the `symbol` is the key and the other attributes are nested inside `symbol`. The nested keys are `name`, `number`, `row`, `column`.

To populate your dictionary with data, provide a menu of options to the users:

1. Search the element by symbol (see all the details).
2. Search by a property (`name`, `number`, `row`, `column`) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program
`````
CODE:
import json
d={'He':{'name':'Helium','atomic_number':'2','row':'3','column':'4'},
   'H':{'name':'Hydrogen','atomic_number':'1','row':'5','column':'6'}}
di={}
ans=True
while ans:
    print ("""
    1. Search the element by symbol (see all the details).
    2. Search by a property (`name`, `number`, `row`, `column`) and see the
    values for that property for all the elements in the table.
    3. Enter a new element manually (type the information for each property)
    4. Change the properties of an element (by symbol)
    5. Export periodic table as a JSON file
    6. Load periodic table from JSON file
    7. Exit the program""")
    ans=input("What would you like to do? ") 
    if ans=="1":
      sy=input('Enter the element symbol to search:')
      sy=sy.capitalize()
      if sy in di.keys():
          print(di[sy])
      else:
          print("The given input symbol is not present in table")
    elif ans=="2":
      pr=input('Enter the element property to search:')
      for i in di.keys():
        print(di[i][pr])
    elif ans=="3":
      s=input("Enter the element symbol:")
      n=input("Enter the name of the element:")
      an=input("Enter the atomic number of the element:")
      r=input("Enter row number:")
      c=input("Enter column number:")
      di[s]={'name':n,'atomic_number':an,'row':r,'column':c}
      print(di)
    elif ans=="4":
      sy=input("Enter symbol of an element you wish to change the property:")
      pr=input("Which property do you want to change?")
      x=input("Please enter new {0} for {1}({2}): ".format(pr,di[sy]['name'],sy))
      di[sy][pr]=x
      print(di)
    elif ans=="5":
      print("\n Goodbye")
    elif ans=="6":
      print("\n Goodbye")
    elif ans=="7":
      exit()
    elif ans !="":
      print("\n Not Valid Choice Try again")
      
OUTPUT:
1.) 1. Search the element by symbol (see all the details).
    2. Search by a property (`name`, `number`, `row`, `column`) and see the
    values for that property for all the elements in the table.
    3. Enter a new element manually (type the information for each property)
    4. Change the properties of an element (by symbol)
    5. Export periodic table as a JSON file
    6. Load periodic table from JSON file
    7. Exit the program
What would you like to do? 3
Enter the element symbol:H
Enter the name of the element:Hydrogen
Enter the atomic number of the element:1
Enter row number:1
Enter column number:1
{'H': {'name': 'Hydrogen', 'atomic_number': '1', 'row': '1', 'column': '1'}}
2.) 1. Search the element by symbol (see all the details).
    2. Search by a property (`name`, `number`, `row`, `column`) and see the
    values for that property for all the elements in the table.
    3. Enter a new element manually (type the information for each property)
    4. Change the properties of an element (by symbol)
    5. Export periodic table as a JSON file
    6. Load periodic table from JSON file
    7. Exit the program
What would you like to do? 1
Enter the element symbol to search:He
{'name': 'Helium', 'atomic_number': '2', 'row': '1', 'column': '18'}
3.)1. Search the element by symbol (see all the details).
    2. Search by a property (`name`, `number`, `row`, `column`) and see the
    values for that property for all the elements in the table.
    3. Enter a new element manually (type the information for each property)
    4. Change the properties of an element (by symbol)
    5. Export periodic table as a JSON file
    6. Load periodic table from JSON file
    7. Exit the program
What would you like to do? 2
Enter the element property to search:name
Helium
4.)1. Search the element by symbol (see all the details).
    2. Search by a property (`name`, `number`, `row`, `column`) and see the
    values for that property for all the elements in the table.
    3. Enter a new element manually (type the information for each property)
    4. Change the properties of an element (by symbol)
    5. Export periodic table as a JSON file
    6. Load periodic table from JSON file
    7. Exit the program
What would you like to do? 4
Enter symbol of an element you wish to change the property:He
Which property do you want to change?r
Please enter new r for Helium(He): 01
{'He': {'name': 'Helium', 'atomic_number': '2', 'row': '1', 'column': '1', 'r': '01'}}
5.) 1. Search the element by symbol (see all the details).
    2. Search by a property (`name`, `number`, `row`, `column`) and see the
    values for that property for all the elements in the table.
    3. Enter a new element manually (type the information for each property)
    4. Change the properties of an element (by symbol)
    5. Export periodic table as a JSON file
    6. Load periodic table from JSON file
    7. Exit the program
What would you like to do? 5

 Goodbye


 6.)1. Search the element by symbol (see all the details).
    2. Search by a property (`name`, `number`, `row`, `column`) and see the
    values for that property for all the elements in the table.
    3. Enter a new element manually (type the information for each property)
    4. Change the properties of an element (by symbol)
    5. Export periodic table as a JSON file
    6. Load periodic table from JSON file
    7. Exit the program
What would you like to do? 6

 Goodbye



      

`````
