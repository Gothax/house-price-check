import pandas as pd

data = pd.read_excel('data/output_usethis.xlsx')


for idx, comp in data.iterrows():
    if comp['경도'] == None:
        print(comp['경도'])
        print(idx)