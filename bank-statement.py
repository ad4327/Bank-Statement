# BANK STATEMENT SCRAPE
import pandas as pd
import numpy as np
import re

#Read CSV Bank Statement file (Download this from your bank account)
df = pd.read_csv('bank statement.csv')

#Drop unwanted columns
df = df.drop(columns=['Bank Account', 'Categories', 'Serial'])

#Month Names
months = '|'.join(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])
#Create a pattern of which descriptive words to drop in narrative column
pattern = '|'.join(['DEBIT', 'CARD', 'PURCHASE', 'EFTPOS', 'DEPOSIT', 'WITHDRAWAL-OSKO', 'WITHDRAWAL',
                    'PAYMENT', 'AUS', 'GROUP', 'PTY', 'LTD', '\d+', months])

#Drop any strings that contain any of the words in the pattern variable
df['Narrative'] = df['Narrative'].str.replace(pattern, '')

#Create a list of locations you use your purchases
newval = ['DARWIN', 'PALMERSTON','CASUARINA', 'COOLALINGA', 'PARAP','KARAMA', 'RAPID CREEK', 'MARARA',
          'THE GARDENS', 'GOLD COAST', 'SURFERS PARADISE', 'BROADBEACH', 'SOUTHPORT',
          'SOUTHBANK', 'OXENFORD', 'BRISBANE', 'SYDNEY', 'CHATSWOOD']


conditions = [
    df['Narrative'].str.contains('DARWIN', flags=re.IGNORECASE),
    df['Narrative'].str.contains('CBD', flags=re.IGNORECASE),
    df['Narrative'].str.contains('PALMERSTON', flags=re.IGNORECASE),
    df['Narrative'].str.contains('CASUARINA', flags=re.IGNORECASE),
    df['Narrative'].str.contains('COOLALINGA', flags=re.IGNORECASE),
    df['Narrative'].str.contains('PARAP', flags=re.IGNORECASE),
    df['Narrative'].str.contains('KARAMA', flags=re.IGNORECASE),
    df['Narrative'].str.contains('RAPID CREEK', flags=re.IGNORECASE),
    df['Narrative'].str.contains('RARA', flags=re.IGNORECASE),
    df['Narrative'].str.contains('THE GARDENS', flags=re.IGNORECASE),
    df['Narrative'].str.contains('FANNIE BAY', flags=re.IGNORECASE),
    df['Narrative'].str.contains('BERRY SPRINGS', flags=re.IGNORECASE),
    df['Narrative'].str.contains('KATHERINE', flags=re.IGNORECASE),
    df['Narrative'].str.contains('LYONS', flags=re.IGNORECASE),
    df['Narrative'].str.contains('COCONUT', flags=re.IGNORECASE),
    df['Narrative'].str.contains('JINGILI', flags=re.IGNORECASE),
    df['Narrative'].str.contains('LEANYER', flags=re.IGNORECASE),
    df['Narrative'].str.contains('STUART PARK', flags=re.IGNORECASE),
    df['Narrative'].str.contains('MILLNER', flags=re.IGNORECASE),
    df['Narrative'].str.contains('NIGHT', flags=re.IGNORECASE),
    df['Narrative'].str.contains('WINNELLIE', flags=re.IGNORECASE),
    df['Narrative'].str.contains('BAYVIEW', flags=re.IGNORECASE),
    df['Narrative'].str.contains('LUDMILLA', flags=re.IGNORECASE),
    df['Narrative'].str.contains('WAGAMAN', flags=re.IGNORECASE),
    df['Narrative'].str.contains('NAKARA', flags=re.IGNORECASE),
    df['Narrative'].str.contains('BERRIMAH', flags=re.IGNORECASE),
    df['Narrative'].str.contains('JABIRU', flags=re.IGNORECASE),
    df['Narrative'].str.contains('MATARANKA', flags=re.IGNORECASE),
    df['Narrative'].str.contains('WANGURI', flags=re.IGNORECASE),
    df['Narrative'].str.contains('NT MEDICAL', flags=re.IGNORECASE),
    df['Narrative'].str.contains('GOLD CO', flags=re.IGNORECASE),
    df['Narrative'].str.contains('SURFERS', flags=re.IGNORECASE),
    df['Narrative'].str.contains('BROADBEA', flags=re.IGNORECASE),
    df['Narrative'].str.contains('SOUTHPORT', flags=re.IGNORECASE),
    df['Narrative'].str.contains('SOUTHBANK', flags=re.IGNORECASE),
    df['Narrative'].str.contains('OXENFORD', flags=re.IGNORECASE),
    df['Narrative'].str.contains('BRISBANE', flags=re.IGNORECASE),
    df['Narrative'].str.contains('SYDNEY', flags=re.IGNORECASE),
    df['Narrative'].str.contains('CHATSWOOD', flags=re.IGNORECASE),
    df['Narrative'].str.contains('BARANGAROO', flags=re.IGNORECASE),
    df['Narrative'].str.contains('YARRAWONGA', flags=re.IGNORECASE),
    df['Narrative'].str.contains('RICHMOND', flags=re.IGNORECASE),
    df['Narrative'].str.contains('EATON', flags=re.IGNORECASE)
    ]

#Create a list of names/places to organise expenditure
values = ['DARWIN', 'PALMERSTON','CASUARINA', 'COOLALINGA', 'PARAP','KARAMA', 'RAPID CREEK', 'MARRARA',
          'FANNIE BAY', 'BERRY SPRINGS', 'KATHERINE', 'LYONS', 'COCONUT GROVE', 'JINGILI',
          'THE GARDENS', 'LEANYER', 'STUART PARK', 'MILLNER', 'NIGHT CLIFF', 'WINNELLIE', 'BAYVIEW', 'LUDMILLA',
          'WAGAMAN', 'NAKARA', 'BERRIMAH', 'JABIRU', 'MATARANKA', 'WANGURI', 'WANGURI',
          'GOLD COAST', 'SURFERS PARADISE', 'BROADBEACH', 'SOUTHPORT', 'SOUTHBANK', 'OXENFORD', 'BRISBANE',
          'SYDNEY', 'CHATSWOOD', 'BARANGAROO',
          'YARRAWONGA', 'RICHMOND',
          'EATON']

#Create which state these locations are in
df['Location'] = np.select(conditions, values, default='DARWIN')
df['State'] = 'NT'


nsw_towns = ['SYDNEY', 'CHATSWOOD', 'BARANGAROO']

nt_towns = ['DARWIN', 'PALMERSTON','CASUARINA', 'COOLALINGA', 'PARAP','KARAMA', 'RAPID CREEK', 'MARRARA',
            'FANNIE BAY', 'BERRY SPRINGS', 'KATHERINE', 'LYONS', 'COCONUT GROVE', 'JINGILI',
          'THE GARDENS', 'LEANYER', 'STUART PARK', 'MILLNER', 'NIGHT CLIFF', 'WINNELLIE', 'BAYVIEW', 'LUDMILLA',
          'WAGAMAN', 'NAKARA', 'BERRIMAH', 'JABIRU', 'MATARANKA', 'WANGURI', 'PALMERSTON', 'YARRAWONGA']

qld_towns = ['GOLD COAST', 'SURFERS PARADISE', 'BROADBEACH', 'SOUTHPORT',
          'SOUTHBANK', 'OXENFORD', 'BRISBANE']

vic_towns = ['RICHMOND']

wa_towns = ['EATON']


df['State'].loc[df['Location'].isin(nsw_towns)] = 'NSW'
df['State'].loc[df['Location'].isin(nt_towns)] = 'NT'
df['State'].loc[df['Location'].isin(qld_towns)] = 'QLD'
df['State'].loc[df['Location'].isin(vic_towns)] = 'VIC'
df['State'].loc[df['Location'].isin(wa_towns)] = 'WA'


#Save to Excel file
df.to_excel('Bank-Statement.xlsx', header=True, index=False)