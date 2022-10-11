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
