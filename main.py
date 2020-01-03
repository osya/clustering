import os

import pandas as pd

geo = pd.read_excel(os.path.join('data', 'geo.xlsx'))
# geo_comment = pd.read_excel(os.path.join('data', 'geo.xlsx'))
print(geo)
