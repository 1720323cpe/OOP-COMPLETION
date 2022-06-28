try:
     menu_items = ('spaghetti', 'sisig', 'beef streak','burger', 'leche flan',)

     print("You can choose from the following menu items:")
     for item in menu_items:
          print("- " + item)

     menu_items = ('spaghetti', 'sisig', 'beef steak', 'fries', 'sundae',)

     print("\nOur menu has been updated.")
     print("You can now choose from the following items:")
     for item in menu_items:
         print("- " + item)
  
except:
    print('error')

finally:
    print('thank you for interacting!')