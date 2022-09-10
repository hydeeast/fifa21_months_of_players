import pandas as pd
import calendar
import matplotlib.pyplot as plt
import imageio
import random

df = pd.read_csv('D:/Coding/data/fifa21/players_21.csv')

#Selecting the leagues we only want to use
leagues = ['English Premier League', 'Spain Primera Division', 'Italian Serie A', 'German 1. Bundesliga', 'French Ligue 1']
df = df[df['league_name'].isin(leagues)]

#Tidying up 'dob' column
df['dob'] = pd.to_datetime(df['dob'])
df['year'] = pd.DatetimeIndex(df['dob']).year
df['month'] = pd.DatetimeIndex(df['dob']).month
df['month_name'] = df['month'].apply(lambda x: calendar.month_abbr[x])
df['day'] = pd.DatetimeIndex(df['dob']).day
df['dayofweek'] = pd.DatetimeIndex(df['dob']).weekday

#What is the distribution of the birth months in the dataset?
(df['month'].value_counts(normalize=True)*100).sort_index().plot()
#The X axis shows month of year.
#The Y axis shows the % of players in the dataset born in that month.

#defining random colour for leagues
def return_random_hex():
    r = lambda: random.randint(0,255)
    return ('#%02X%02X%02X' % (r(), r(), r()))


#Loop to create a random hex colour and assign to each league's line and title
for index,league in enumerate(leagues):
    fix, ax = plt.subplots(nrows=1, ncols=1)
    col = return_random_hex()
    for league2 in leagues:
        (df[df['league_name']==league2]
    ['month'].value_counts(normalize=True)*100).sort_index().plot(color = 'gray')
        (df[df['league_name']==league]
    ['month'].value_counts(normalize=True)*100).sort_index().plot(color = col)
        plt.text(1,15,'Players by birth month', fontsize=22, fontweight=300)
        plt.text(1,14,league, fontsize=16, color=col, fontweight=500)
        plt.xlabel('Month')
        plt.ylabel('% Players')
        plt.tight_layout()
        plt.savefig(str(index) + '.png')

#as a gif
with imageio.get_writer('months.gif', mode='I') as writer:
    for index in range(0,5):
        for i in range(0,6):
            image = imageio.v2.imread(str(index) + '.png')
            writer.append_data(image)
