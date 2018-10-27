import quandl
import pandas as pd
import numpy as np
quandl.ApiConfig.api_key = "vUhdxhXJX6syMWsoNeSS"

data = quandl.get("EIA/PET_RWTC_D",returns="pandas")

print(data.head())
print(data.dtypes)

