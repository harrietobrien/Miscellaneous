import pandas as pd

df = pd.DataFrame({'MIMNumber': ['102610', '114080,601079'],
                   'OMIM_Link': ['https://www.omim.org/entry/',
                                 'https://www.omim.org/entry/,https://www.omim.org/entry/']})

result = list()
for i in range(len(df)):
    mim = df['MIMNumber'][i]
    if "," in mim:
        mim = mim.split(",")
        link = df['OMIM_Link'][i].split(",")
        df['OMIM_Link'][i] = ",".join(['{o}{m}'.format(o=link[i], m=mim[i])
                                       for i in range(len(link))])
    else:
        link = df['OMIM_Link'][i]
        df['OMIM_Link'][i] = '{omim}{mim}'.format(omim=link, mim=mim)

# or simply:
df['OMIM_Link'] = 'https://www.omim.org/entry/' + \
                  df['MIMNumber'].str.replace(',', ',https://www.omim.org/entry/')

print(df)
