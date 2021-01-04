import openpyxl as oxl
from datetime import datetime

labelData = {
    'genre': ['Action', 'Adventure', 'Comedy', 'Documentary', 'Drama', 'Horror', 'Musical', 'Romantic', 'Thriller'],
    'theme': ['Animated', 'Crime', 'Fantasy', 'Historical', 'Music', 'SciFi', 'War', 'Western']
    }

entryData = {
    'Title': '', 
    'Director': '', 
    'Genre': [], 
    'Theme': [], 
    'Release': '', 
    'MPAA': '', 
    'Cast': [], 
    'Rating': 0, 
    'Comment': ''
    }

def addData():
    entryData['Title'] = input('Enter the film title: ')
    entryData['Director'] = input('Enter the film director: ')
    
    print(labelData['genre'])
    genreList = []
    while True:
        x = input('Enter a genre from above, or enter 0 to continue: ')
        if x == '0':
            break
        genreList.append(x)
    entryData['Genre'] = genreList

    print(labelData['theme'])
    themeList = []
    while True:
        x = input('Enter a theme from above, or enter 0 to continue: ')
        if x == '0':
            break
        themeList.append(x)
    entryData['Theme'] = themeList

    dateStr = input('Enter the release date (mm/dd/yyyy): ')
    entryData['Release'] = datetime.strptime(dateStr, '%m/%d/%Y')
    
    entryData['MPAA'] = input('Enter the MPAA rating: ')
    
    castList = []
    while True:
        x = input('Enter a cast member, or enter 0 to continue: ')
        if x == '0':
            break
        castList.append(x)
    entryData['Cast'] = castList

    entryData['Rating'] = int(input('Enter personal rating out of 10: '))
    entryData['Comment'] = input('Enter comment if any: ')


addData()

print('Opening workbook...')

wb = oxl.load_workbook('movielist.xlsx')
dbSheet = wb.get_sheet_by_name('Database')

print('Adding data...')
row = 2
while True:
    if dbSheet['A' + str(row)].value == None:
        break
    row += 1

dbSheet['A' + str(row)].value = entryData['Title']
dbSheet['B' + str(row)].value = entryData['Director']
dbSheet['C' + str(row)].value = ', '.join(entryData['Genre'])
dbSheet['D' + str(row)].value = ', '.join(entryData['Theme'])
dbSheet['E' + str(row)].value = entryData['Release']
dbSheet['F' + str(row)].value = entryData['MPAA']
dbSheet['G' + str(row)].value = ', '.join(entryData['Cast'])
dbSheet['H' + str(row)].value = entryData['Rating']
dbSheet['I' + str(row)].value = entryData['Comment']

print('Saving workbook...')
wb.save('movielist.xlsx')