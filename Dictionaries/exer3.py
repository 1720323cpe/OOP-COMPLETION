TM_rivers = {
    'Huang He River': 'China',
    'Mississippi River': 'North America',
    'Congo River': 'Africa',
    }

for river, country in TM_rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
    
#Use a loop to print the name of each river included 
print("\nThe following rivers are included in this data set:")
for river in TM_rivers.keys():
    print(river.title())
    
#Use a loop to print the name of each country included in the dictionary.
print("\nThe following countries are included in this data set:")
for country in TM_rivers.values():
    print(country.title())
