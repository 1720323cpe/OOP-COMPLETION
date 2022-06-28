import csv 

fieldnames = ['name', 'area', 'country_code2', 'country_code3']

rows = [
    {'name': 'Netherlands',
    'area': 41543,
    'country_code2': 'NL',
    'country_code3': 'NLD'},
    {'name': 'Thailand',
    'area': 513120,
    'country_code2': 'TH',
    'country_code3': 'THA'},
    {'name': 'Australia,',
    'area': 7.692,
    'country_code2': 'AU',
    'country_code3': 'AUS'}
]

with open ('countries.csv', 'w', encoding= 'UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)