



string = "June 18th 2020"
year = string[-4:]
string = string[:-len(year)]
string = string.rstrip(' ')
string = string [:-2]
string = string + ' ' + year

print(string)
if month == 'January':
    month = 1
elif month == 'February':
    month = 2
elif month == 'March':
    month 