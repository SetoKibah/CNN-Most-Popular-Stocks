import pandas as pd

scraper = pd.read_html("https://money.cnn.com/data/hotstocks/index.html")
print('S&P 500\n')
print('Most Actives')
print(scraper[0])
print('\n\nGainers')
print(scraper[1])
print('\n\nLosers')
print(scraper[2])


scraper = pd.read_html("https://money.cnn.com/data/hotstocks/sp1500/")
print('\n*******************************************\nS&P 1500\n')
print('Most Actives')
print(scraper[0])
print('\n\nGainers')
print(scraper[1])
print('\n\nLosers')
print(scraper[2])